#!/usr/bin/python
#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        CnblogsFan_GetBlogsURL.py
# Purpose:
#
# Author:      Mr.Wid
#
# Created:     15-10-2012
# Copyright:   (c) Mr.Wid 2012
# Licence:     GNU GPL
#-------------------------------------------------------------------------------

import wx

class SpiderModeDlg(wx.Dialog):
    def __init__( self, parent = None ):
        wx.Dialog.__init__(
            self,
            parent = parent,
            title = u'蜘蛛模式',
            size = (400, 300)
        )
        #-----cnblogs地址标签-----
        self.lblCnblogsUrl = wx.StaticText(
            self,
            label = u'采集地址:',
            pos = ( 60, 30 )
        )
        rect = self.lblCnblogsUrl.Rect
        self.txtCnblogsUrl = wx.TextCtrl(
            self,
            size = ( 200, -1 ),
            pos = ( rect[0] + rect[2] + 10, rect[1] - 3 ),
            value = u'http://www.cnblogs.com',
            style = wx.TE_READONLY
        )
        self.txtCnblogsUrl.Disable()
        #self.line = wx.StaticLine(self, pos = (100, 100), size = (100, 2))

        #-----爬行方式选择-----
        rect = self.lblCnblogsUrl.Rect
        self.groupWorkMode = wx.StaticBox(
            self,
            label = u'遍历方式选择',
            pos = ( rect[0] - 20, rect[1] + 40 ),
            size = ( rect[0] + self.txtCnblogsUrl.Rect[2] + 50, 80 ),
        )
        rect = self.groupWorkMode.Rect
        self.rdoboxWorkMode = wx.RadioBox(
            self,
            choices = [ u'使用深度优先', u'使用广度优先' ],
            style = wx.RA_HORIZONTAL,
        )
        self.rdoboxWorkMode.Position = (
            rect[0] + (rect[2] - self.rdoboxWorkMode.Rect[2]) / 2 ,
            rect[1] + (rect[3] - self.rdoboxWorkMode.Rect[3]) / 2
        )

        #-----下一步按钮-----
        self.btnNextStep = wx.Button(
            self,
            label = u'下一步',
            size = (80, 50),
        )
        self.btnNextStep.Position = (
            (self.ClientRect[2] - self.btnNextStep.Rect[2]) / 2 ,
            rect[1] + rect[3] + 50
        )

        #-----事件绑定-----
        self.Bind( wx.EVT_BUTTON, self.OnNextStep, self.btnNextStep )           #绑定"下一步"按钮事件

    #"下一步"按钮的事件响应, 销毁对话框并返回选择的遍历方式
    def OnNextStep( self, evt ):
        self.Destroy()
        return self.rdoboxWorkMode.GetSelection()


class SelectUserBlogDlg(wx.Dialog):
    def __init__( self, parent = None ):
        wx.Dialog.__init__(
            self,
            parent = parent,
            title = u'指定采集',
            size = (400, 300)
        )
        #-----cnblogs地址标签-----
        self.lblCnblogsUrl = wx.StaticText(
            self,
            label = u'采集地址:',
            pos = ( 30, 30 )
        )
        rect = self.lblCnblogsUrl.Rect
        self.txtCnblogsUrl = wx.TextCtrl(
            self,
            size = ( 260, 150 ),
            pos = ( rect[0] + rect[2] + 10, rect[1] - 3 ),
            value = u'每行一个博客地址',
            style = wx.TE_MULTILINE
        )
        self.tipValue = True

        #-----"下一步"按钮-----
        self.btnNextStep = wx.Button(
            self,
            label = u'下一步',
            size = (80, 50),
        )
        self.btnNextStep.Position = (
            (self.ClientRect[2] - self.btnNextStep.Rect[2]) / 2 ,
            rect[1] + rect[3] + 150
        )

        #-----事件绑定-----
        #--绑定鼠标在文本框按下事件, 响应方法self.OnClearTipValue
        self.txtCnblogsUrl.Bind( wx.EVT_LEFT_DOWN, self.OnClearTipValue )
        #--绑定"下一步"按钮方法
        self.Bind( wx.EVT_BUTTON, self.OnNextStep, self.btnNextStep )

    #清除文本框中的提示文字
    def OnClearTipValue( self, evt ):
        if self.tipValue:
            self.txtCnblogsUrl.SetValue(u'')
            self.tipValue = False

    def OnNextStep( self, evt ):
        self.Destroy()
        return self.txtCnblogsUrl.GetValue()


class UseClassificationDlg(wx.Dialog):
    def __init__( self, parent = None ):
        wx.Dialog.__init__(
            self,
            parent = parent,
            title = u'分类采集',
            size = (400, 300)
        )
        #-----分类复选框-----
        self.groupSelectBox = wx.StaticBox(
            self,
            label = u'选择分类',
            pos = ( 20, 20 ),
            size = ( 350, 120 ),
        )
        #--所有分类
        allType= [
            u'首页随笔',
            u'精华随笔',
            u'候选随笔',
            u'推荐博客',
            u'专家博客',
            u'全部选择'
        ]
        x, y = self.groupSelectBox.Rect[0] + 40, self.groupSelectBox.Rect[1] + 30
        self.SelectType = []
        for i in range( len(allType) ):
            self.SelectType.append(
                wx.CheckBox(
                    self,
                    label = allType[i],
                    pos = ( x, y )
                )
            )
            x += 100
            if x > 300:
                x = self.groupSelectBox.Rect[0] + 40
                y += 50

        #--下一步按钮
        #-----"下一步"按钮-----
        self.btnNextStep = wx.Button(
            self,
            label = u'下一步',
            size = (80, 50),
        )
        self.btnNextStep.Position = (
            (self.ClientRect[2] - self.btnNextStep.Rect[2]) / 2 ,
            self.ClientRect[3] - 100
        )

        #-----事件绑定-----
        self.Bind( wx.EVT_BUTTON, self.OnNextStep, self.btnNextStep )

    def OnNextStep( self, evt ):
        self.Destroy()



def test():
    app = wx.PySimpleApp()
    dlg = UseClassificationDlg()
    dlg.ShowModal()

if __name__ == '__main__':
    test()