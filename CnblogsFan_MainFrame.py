#!/usr/bin/python
#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        CnblogsFan_MainFrame.py
# Purpose:
#
# Author:      Mr.Wid
#
# Created:     13-10-2012
# Copyright:   (c) Mr.Wid 2012
# Licence:     GNU GPL
#-------------------------------------------------------------------------------

import wx
import CnblogsFan_GetArgumentsDlg

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(
            self,
            parent = None,
            title = u'CnblogsFan',
            size = (( 900, 600 )),
            style = wx.SYSTEM_MENU|wx.CAPTION|wx.MINIMIZE_BOX|wx.CLOSE_BOX
        )
        self.Center()                                                           #居中显示

        #-----加载程序图标-----
        self.AppLogo = wx.Icon('src\ICON_CnblogsFan.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.AppLogo)

        #-----创建面板-----
        self.panel = wx.Panel(self)

        #-----创建状态栏-----
        self.userStatus = self.CreateStatusBar()
        self.userStatus.SetFieldsCount(4)
        self.userStatus.SetStatusWidths( [-1, -1, -1, -1] )
        #--
        statusLabel = [
            u' 当前状态:',
            u' 采集速度:',
            u' 采集统计:',
            u' 任务统计:',
        ]
        for i in range( len(statusLabel) ):
            self.userStatus.SetStatusText( statusLabel[i], i )

        #-----创建菜单栏-----
        self.groupMenuBox = wx.StaticBox(
            self.panel,
            label = u'菜单',
            pos = (15, 10),
            size = (80, 400),
        )
        #--加载菜单图标
        self.localImgSrc = [
            'CnblogsFan_Spider.png',
            'CnblogsFan_Single.png',
            'CnblogsFan_Classify.png',
            'CnblogsFan_Setting.png',
            'CnblogsFan_About.png'
        ]
        self.lstMenu = []                                                       #菜单列表
        menuTip = [
            u'采集整个Cnblogs上的随笔.',
            u'采集指定博客上的随笔.',
            u'采集Cnblogs首页分类上的随笔.',
            u'设置软件的相关参数.',
            u'关于CnblogsFan的一些信息.'
        ]
        menuLabel = [
            u'蜘蛛模式',
            u'指定采集',
            u'分类采集',
            u'软件设置',
            u'关于软件'
        ]
        rect = self.groupMenuBox.Rect
        x, y = rect[0] + ( rect[2]-48 )/2, rect[1] * 3
        for i in range( len(self.localImgSrc) ):
            tempImg = wx.Image( 'src\\'+ self.localImgSrc[i], wx.BITMAP_TYPE_ANY )
            w, h = tempImg.GetSize()
            img = tempImg.Scale( w*0.8, h*0.8 )
            self.lstMenu.append(
                wx.BitmapButton(
                    self.panel,
                    bitmap = img.ConvertToBitmap(),
                    pos = ( x, y )
                )
            )
            #--为按钮增加标签
            self.lblMenu = wx.StaticText(
                                self.panel,
                                label = menuLabel[i],
                                pos = ( x, y + 50 )
                            )
            y += self.lstMenu[i].Rect[0] + 45
            #--增加按钮提示信息
            self.lstMenu[i].SetToolTipString(menuTip[i])

        #------创建当前采集用户信息栏-----
        rect = self.groupMenuBox.Rect
        self.groupBlogsUserInfoBox = wx.StaticBox(
            self.panel,
            label = u'当前所在博客博主信息',
            pos = ( rect[0] + rect[2]+ 20, rect[1] ),
            size = ( 500, 100 )
        )
        #--用户信息标签
        adminInfoLabel = [
            u'昵称:',
            u'园龄:',
            u'粉丝:',
            u'关注:',
            u'随笔:',
            u'文章:',
            u'评论:',
            u'地址:'
        ]
        self.lstAdminInfo = []
        rect = self.groupBlogsUserInfoBox.Rect
        x, y = rect[0] + 20, rect[1] + 30
        for i in range(len(adminInfoLabel)):
            self.lstAdminInfo.append(
                wx.StaticText(
                    self.panel,
                    label = adminInfoLabel[i],
                    pos = ( x, y )
                )
            )
            x += 150
            if x > 450:
                x = rect[0] + 20
                y += 20

        #-----创建任务控制栏-----
        rect = self.groupBlogsUserInfoBox.Rect
        self.groupControlBox = wx.StaticBox(
            self.panel,
            label = u'任务控制',
            pos = ( rect[0] + rect[2]+ 20, rect[1] ),
            size = ( 230, 100 )
        )
        #--控制按钮
        self.btnPauseContinue = wx.Button(
            self.panel,
            label = u'暂停',
            size = ( 60, 60 ),
            pos = ( rect[0] + rect[2]+ 50, rect[1] + 25 )
        )
        self.btnPauseContinue.Disable()
        rect = self.btnPauseContinue.Rect
        self.btnStop = wx.Button(
            self.panel,
            label = u'停止',
            size = ( 60, 60 ),
            pos = ( rect[0] + rect[2]+ 50, rect[1] )
        )
        self.btnStop.Disable()

        #-----成功采集信息栏-----
        rect = self.groupBlogsUserInfoBox.Rect
        self.groupSucceedBox = wx.StaticBox(
            self.panel,
            label = u'成功采集',
            pos = ( rect[0], rect[1] + rect[3] + 20 ),
            size = ( 750, 280 )
        )
        #--成功采集列表
        rect = self.groupSucceedBox.Rect
        self.lstSucceedResults = wx.ListCtrl(
            self.panel,
            pos = ( rect[0] + 10, rect[1] + 20 ),
            style = wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES,
            size = ( rect[2] - 20, rect[3] - 30 )
        )
        w = self.lstSucceedResults.Rect[2]
        self.lstSucceedResults.InsertColumn( col = 0, heading = u'随笔名称', width = w * 0.3 )
        self.lstSucceedResults.InsertColumn( col = 1, heading = u'来源地址', width = w * 0.5 )
        self.lstSucceedResults.InsertColumn( col = 2, heading = u'发布时间', width = w * 0.15 )

        #-----成功采集信息栏-----
        rect = self.groupSucceedBox.Rect
        self.groupActionBox = wx.StaticBox(
            self.panel,
            label = u'当前动作',
            pos = ( rect[0], rect[1] + rect[3] + 20 ),
            size = ( 750, 110 )
        )
        #--动作输出文本框
        rect = self.groupActionBox.Rect
        self.txtFeedback = wx.TextCtrl(
            self.panel,
            size = ( rect[2] - 20, rect[3] - 30 ),
            pos = ( rect[0] +10, rect[1] + 20 ),
            style = wx.TE_MULTILINE | wx.TE_READONLY
        )

        #-----意见反馈栏-----
        rect = self.groupMenuBox.Rect
        self.groupFeedbackBox = wx.StaticBox(
            self.panel,
            label = u'告诉作者',
            pos = ( rect[0], rect[1] + rect[3] + 20 ),
            size = ( rect[2], 110 ),
        )
        #--意见输入文本框
        rect = self.groupFeedbackBox.Rect
        self.txtFeedback = wx.TextCtrl(
            self.panel,
            size = ( rect[2] - 10, rect[3] - 50 ),
            pos = ( rect[0] + 5, rect[1] + 20 ),
            style = wx.TE_MULTILINE
        )
        #--提交按钮
        self.txtFeedback.SetMaxLength(1024)
        rect = self.txtFeedback.Rect
        self.btnFeedback = wx.Button(
            self.panel,
            label = u'提交',
            pos = ( rect[0], rect[1] + rect[3] + 5 ),
            size = (rect[2], 20)
        )


        #-----事件绑定-----
        #--菜单按钮事件
        self.Bind( wx.EVT_BUTTON, self.OnSelectSpiderMode, self.lstMenu[0] )    #绑定蜘蛛模式按钮, 响应方法:self.OnSelectSpiderMode
        self.Bind( wx.EVT_BUTTON, self.OnSelectUserBlogMode, self.lstMenu[1] )  #绑定蜘蛛模式按钮, 响应方法:self.OnSelectUserBlogMode
        self.Bind( wx.EVT_BUTTON, self.OnSelectUseKindsMode, self.lstMenu[2] )  #绑定蜘蛛模式按钮, 响应方法:self.OnSelectUseKindsMode


    #-----事件响应-----
    #--菜单按钮事件响应
    #响应菜单"蜘蛛模式"按钮
    def OnSelectSpiderMode( self, evt ):
        dlg = CnblogsFan_GetArgumentsDlg.SpiderModeDlg(self)
        dlg.ShowModal()
    #响应菜单"指定采集"按钮
    def OnSelectUserBlogMode( self, evt ):
        dlg = CnblogsFan_GetArgumentsDlg.SelectUserBlogDlg(self)
        dlg.ShowModal()
    #响应菜单"分类采集"按钮
    def OnSelectUseKindsMode( self, evt ):
        dlg = CnblogsFan_GetArgumentsDlg.UseClassificationDlg(self)
        dlg.ShowModal()



def test():
    cnblogsFan = wx.PySimpleApp()
    mainFrame = MainFrame()
    mainFrame.Show()
    cnblogsFan.MainLoop()

if __name__ == '__main__':
    test()
