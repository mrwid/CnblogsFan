#!/usr/bin/python
#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        CnblogsFan_SettingDlg.py
# Purpose:
#
# Author:      Mr.Wid
#
# Created:     17-10-2012
# Copyright:   (c) Mr.Wid 2012
# Licence:     GNU GPL
#-------------------------------------------------------------------------------

import wx

class SettingDlg(wx.Dialog):
    def __init__( self, parent = None ):
        wx.Dialog.__init__(
            self,
            parent = parent,
            title = u'设置',
            size = ( 500, 300 )
        )

        #-----设置保存目录-----
        rect = self.GetClientRect()
        self.groupSaveBox = wx.StaticBox(
            self,
            label = u'采集保存目录设置',
            pos = ( rect[0] + 20 , rect[1] + 20 ),
            size = ( rect[2] - 40, rect[3] - 200 ),
        )
        #--提示标签
        rect = self.groupSaveBox.Rect
        lblSelectTip = wx.StaticText(
            self,
            label = u'请选择默认保存目录:'
        )
        lblSelectTip.SetPosition( ( rect[0]+ 20 , rect[1] +  (rect[3] - lblSelectTip.Rect[3] ) / 2 ) )
        #--路径文本框
        rect = lblSelectTip.Rect
        self.txtPath = wx.TextCtrl(
            self,
            size = ( 200, -1 ),
            pos = ( rect[0] + rect[2] + 10, rect[1] - 3 )
        )
        #--选择目录按钮
        rect = self.txtPath.Rect
        self.btnSelectPath = wx.Button(
            self,
            label = u'浏览目录',
            size = ( 80, rect[3] + 5 ),
            pos = ( rect[0] + rect[2] + 10, rect[1] - 3 )
        )
        #-----完成提示-----
        rect = self.groupSaveBox.Rect
        self.groupTipBox = wx.StaticBox(
            self,
            label = u'任务完成提示设置',
            pos = ( rect[0] , rect[1] + rect[3] + 10 ),
            size = ( rect[2], rect[3] )
        )
        self.chkSoundTip = wx.CheckBox(
            self,
            label = u'声音提示'
        )
        rect = self.groupTipBox.Rect
        self.chkSoundTip.SetPosition( ( rect[0] + 30, rect[1] + (rect[3] - self.chkSoundTip.Rect[3]) / 2 + 5 ) )
        self.chkWindowTip = wx.CheckBox(
            self,
            label = u'窗口提示'
        )
        rect = self.chkSoundTip.Rect
        self.chkWindowTip.SetPosition( ( rect[0] + rect[2] + 30, rect[1] ) )

        #-----保存取消按钮-----
        rect = self.GetClientRect()
        self.btnSaveSetting = wx.Button(
            self,
            label = u'保存设置',
            size = ( 80, 30 )
        )
        self.btnCancelSetting = wx.Button(
            self,
            label = u'取消',
            size = ( 80, 30 )
        )
        self.btnSaveSetting.SetPosition( ( ( rect[2] - self.btnCancelSetting.Rect[2] ) / 2 - 80 , rect[3] - 50  ) )
        self.btnCancelSetting.SetPosition( ( ( rect[2] + self.btnCancelSetting.Rect[2] ) / 2, rect[3] - 50  ) )


def test():
    app = wx.PySimpleApp()
    dlg = SettingDlg()
    dlg.ShowModal()

if __name__ == '__main__':
    test()