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

class MainFrame(wx.Frame):              #从wx.Frame类得到继承
    def __init__(self):                 #初始化窗口
        wx.Frame.__init__(
            self,
            parent = None,              #无父窗口
            title = u'CnblogsFan',      #窗口标题:'CnblogsFan',
            size = ( ( 900, 600 ) ),    #窗口大小900x600
            style = wx.SYSTEM_MENU|wx.CAPTION|wx.MINIMIZE_BOX|wx.CLOSE_BOX      #带有最小化与最大化按钮的窗口样式
        )
        self.Center()                                                           #令窗口在屏幕中居中显示

        #-----加载程序图标-----
        self.AppLogo = wx.Icon('src\ICON_CnblogsFan.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.AppLogo)

        #-----创建窗口面板-----
        self.panel = wx.Panel(self)

        #-----创建状态栏-----
        self.userStatus = self.CreateStatusBar()
        self.userStatus.SetFieldsCount(4)                   #将状态栏分为4部分
        self.userStatus.SetStatusWidths( [-1, -1, -1, -1] ) #划分比例为4等分
        #--
        #状态栏上待显示的文字
        statusLabel = [
            u' 当前状态:',
            u' 采集速度:',
            u' 采集统计:',
            u' 任务统计:',
        ]
        #将文字标签显示在状态栏上
        for i in range( len(statusLabel) ):
            self.userStatus.SetStatusText( statusLabel[i], i )

        #-----创建菜单栏外框StaticBox-----     #这个StaticBox控件为首个控件
        self.groupMenuBox = wx.StaticBox(
            self.panel,
            label = u'菜单',
            pos = (15, 10),                     #在首个控件处使用绝对坐标
            size = (80, 400),                   #框大小为80x400
        )
        #--以下为菜单图标在本地的文件名
        self.localImgSrc = [
            'CnblogsFan_Spider.png',
            'CnblogsFan_Single.png',
            'CnblogsFan_Classify.png',
            'CnblogsFan_Setting.png',
            'CnblogsFan_About.png'
        ]
        self.lstMenu = []                   #菜单列表, 用来记录菜单按钮控件
        menuTip = [
            u'采集整个Cnblogs上的随笔.',    #当鼠标放在按钮上的相关提示文字
            u'采集指定博客上的随笔.',
            u'采集Cnblogs首页分类上的随笔.',
            u'设置软件的相关参数.',
            u'关于CnblogsFan的一些信息.'
        ]                                   #菜单按钮下方的文字说明
        menuLabel = [
            u'蜘蛛模式',
            u'指定采集',
            u'分类采集',
            u'软件设置',
            u'关于软件'
        ]
        rect = self.groupMenuBox.Rect       #获取第一个控件self.groupMenuBox的RECT结构

        #x, y用来决定菜单按钮的位置
        #x = 上个控件的x坐标 + (上个控件的x方向宽度 - 一个按钮的宽度) / 2, 这样按钮控件就能够在groupMenuBox框中居中显示了
        #y = 上个控件在y方向上的坐标的三倍
        x, y = rect[0] + ( rect[2]-48 )/2, rect[1] * 3
        for i in range( len(self.localImgSrc) ):        #for 循环生成按钮控件
            tempImg = wx.Image( 'src\\'+ self.localImgSrc[i], wx.BITMAP_TYPE_ANY )      #从本地加载图标文件
            w, h = tempImg.GetSize()                    #获取加载到的图标尺寸
            img = tempImg.Scale( w*0.8, h*0.8 )         #将图像缩放至80%
            self.lstMenu.append(                        #创建一个菜单按钮并将其加入到菜单按钮列表中
                wx.BitmapButton(
                    self.panel,
                    bitmap = img.ConvertToBitmap(),     #将缩放后的按钮图片转换为位图
                    pos = ( x, y )
                )
            )
            #--为每个按钮增加标签
            wx.StaticText(
                self.panel,
                label = menuLabel[i],
                pos = ( x, y + 50 )                      #之所以令y再加50是为了能够让每个标签显示在按钮的下方, 而不是上方, 50这个值是经过测量按钮RECT结构的值得到
            )
            y += self.lstMenu[i].Rect[0] + 45
            #--为每个按钮增加按钮提示信息
            self.lstMenu[i].SetToolTipString(menuTip[i])

        #在完成一个控件的创建之后下面的创建算法就同上面的了
        #------创建当前采集用户信息栏-----
        rect = self.groupMenuBox.Rect                   #获取上一个控件RECT结构
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
        self.lstAdminInfo = []                          #当前采集用户信息列表
        rect = self.groupBlogsUserInfoBox.Rect          #获取self.groupBlogsUserInfoBox的RECT结构
        x, y = rect[0] + 20, rect[1] + 30
        for i in range(len(adminInfoLabel)):            #生成标签控件
            self.lstAdminInfo.append(                   #将标签控件增添到lstAdminInfo列表当中
                wx.StaticText(
                    self.panel,
                    label = adminInfoLabel[i],
                    pos = ( x, y )
                )
            )
            x += 150                #每个用户信息标签直接间隔150个单位
            if x > 450:             #当放够3个标签后换行放置另外3个标签
                x = rect[0] + 20
                y += 20

        #-----创建任务控制栏-----                       #用来控制在任务进行中的暂停/停止动作
        rect = self.groupBlogsUserInfoBox.Rect
        self.groupControlBox = wx.StaticBox(            #创建静态框StaticBox
            self.panel,
            label = u'任务控制',
            pos = ( rect[0] + rect[2]+ 20, rect[1] ),   #位置在当前采集用户的标签的左侧
            size = ( 230, 100 )
        )
        #--控制按钮
        self.btnPauseContinue = wx.Button(              #创建暂停按钮, 当在任务过程中按下"暂停"后, 暂停标签还要能够变成"继续"
            self.panel,
            label = u'暂停',
            size = ( 60, 60 ),                          #按钮大小
            pos = ( rect[0] + rect[2]+ 50, rect[1] + 25 )   #位置
        )
        self.btnPauseContinue.Disable()                 #在未进行任务前将按钮设为不可用
        rect = self.btnPauseContinue.Rect
        self.btnStop = wx.Button(                       #创建"停止"按钮, 用来中途中断任务的进行
            self.panel,
            label = u'停止',
            size = ( 60, 60 ),
            pos = ( rect[0] + rect[2]+ 50, rect[1] )
        )
        self.btnStop.Disable()                          #按钮不可用

        #-----成功采集信息栏-----                       #用于输出成功采集到的随笔信息
        rect = self.groupBlogsUserInfoBox.Rect
        self.groupSucceedBox = wx.StaticBox(            #静态框
            self.panel,
            label = u'成功采集',
            pos = ( rect[0], rect[1] + rect[3] + 20 ),
            size = ( 750, 280 )
        )
        #--成功采集列表
        rect = self.groupSucceedBox.Rect
        self.lstSucceedResults = wx.ListCtrl(           #创建成功采集列表框
            self.panel,
            pos = ( rect[0] + 10, rect[1] + 20 ),
            style = wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES,
            size = ( rect[2] - 20, rect[3] - 30 )
        )
        w = self.lstSucceedResults.Rect[2]              #获取列表框x方向宽度
        self.lstSucceedResults.InsertColumn( col = 0, heading = u'随笔名称', width = w * 0.3 )      #创建是三个纵列, 分割比例为3:5:1.5, 为了美观留下0.5给竖直滚动条
        self.lstSucceedResults.InsertColumn( col = 1, heading = u'来源地址', width = w * 0.5 )
        self.lstSucceedResults.InsertColumn( col = 2, heading = u'发布时间', width = w * 0.15 )

         #用来告知用户当前正在进行的动作
        #-----当前动作信息栏-----
        rect = self.groupSucceedBox.Rect
        self.groupActionBox = wx.StaticBox(
            self.panel,
            label = u'当前动作',
            pos = ( rect[0], rect[1] + rect[3] + 20 ),
            size = ( 750, 110 )
        )
        #--动作输出文本框, 使用文本框进行当前动作输出
        rect = self.groupActionBox.Rect
        self.txtFeedback = wx.TextCtrl(
            self.panel,
            size = ( rect[2] - 20, rect[3] - 30 ),
            pos = ( rect[0] +10, rect[1] + 20 ),
            style = wx.TE_MULTILINE | wx.TE_READONLY        #带有竖直方向的滚动条并且将文本框设为只读模式
        )

        #在菜单创建栏的下方还剩一个比较小的角落, 用来作为用户反馈意见的位置
        #-----意见反馈栏-----
        rect = self.groupMenuBox.Rect
        self.groupFeedbackBox = wx.StaticBox(
            self.panel,
            label = u'告诉作者',
            pos = ( rect[0], rect[1] + rect[3] + 20 ),
            size = ( rect[2], 110 ),
        )
        #--创建意见输入文本框
        rect = self.groupFeedbackBox.Rect
        self.txtFeedback = wx.TextCtrl(
            self.panel,
            size = ( rect[2] - 10, rect[3] - 50 ),
            pos = ( rect[0] + 5, rect[1] + 20 ),
            style = wx.TE_MULTILINE
        )
        #--创建提交按钮
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
