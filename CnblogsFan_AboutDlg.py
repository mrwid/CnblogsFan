#!/usr/bin/python
#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        CnblogsFan_AboutDlg.py
# Purpose:
#
# Author:      Mr.Wid
#
# Created:     17-10-2012
# Copyright:   (c) Mr.Wid 2012
# Licence:     GNU GPL
#-------------------------------------------------------------------------------

import wx

CnblogsFan_Introduction = u'''CnblogsFan是一款完全开源的绿色软件, 用于采集Cnblogs(博客园)上的随笔.

*蜘蛛模式:
    采集Cnblogs上的所有随笔。

*指定采集：
    采集指定用户的随笔。

*分类采集：
    采集首页的各大分类中的随笔。

*过滤功能:
    轻松找到令您感兴趣的随笔。

作者:   Mr.Wid
博客:   http://www.cnblogs.com/mr-wid
E-mail: mr_wid@163.com
'''

CnblogsFan_License = u'''采用GNU General Public License version 3开源协议.

协议在线阅读:
    http://www.gnu.org/licenses/gpl-3.0.html

CnblogsFan项目下载:
    https://github.com/mrwid/CnblogsFan
'''

CnblogsFan_Others = '''
'''

class AboutDlg(wx.Dialog):
    def __init__( self, parent = None ):
        wx.Dialog.__init__(
            self,
            parent = parent,
            title = u'关于',
            size = (400, 500)
        )
        self.lblImage()
        self.boxInf()
    #-----创建控件-----
    #--CnblogsFan文字图片
    def lblImage(self):
        img = wx.Image('src/CnblogsFan_TextCnblogsFan.png', wx.BITMAP_TYPE_ANY)
        width = img.GetWidth()
        CnblogsFanImage = wx.StaticBitmap(
            self,
            -1,
            wx.BitmapFromImage(img),
            pos = ( (400 - width) / 2 - 5, 20 )
        )
    #--软件信息
    def boxInf(self):
        self.groupBox = wx.StaticBox(
            self,
            label = u'信息',
            pos = ( 15, 110 ),
            size = ( 365, 140 )
        )
        rect = self.groupBox.Rect
        self.lblVersion = wx.StaticText(
            self,
            label = u'版本:    1.0.0',
            pos = ( rect[0] + 20, rect[1] + 30 )
        )
        rect = self.lblVersion.Rect
        self.lblAuthor = wx.StaticText(
            self,
            label = u'作者:    Mr.Wid',
            pos = ( rect[0], rect[1] + 25 )
        )
        rect = self.lblAuthor.Rect
        self.lblWidEmail = wx.StaticText(
            self,
            label = u'E-mail:',
            pos = ( rect[0], rect[1] + 25 )
        )
        rect = self.lblWidEmail.Rect
        self._lblLinkWid = wx.HyperlinkCtrl(
            self,
            id = -1,
            label = u'mr_wid@163.com',
            url = u'mailto:mr_wid@163.com',
            pos = ( rect[0] + rect[2] + 10, rect[1] )
        )
        rect = self.lblWidEmail.Rect
        self.lblWidBlog = wx.StaticText(
            self,
            label = u'博客:    ',
            pos = ( rect[0], rect[1] + 25 )
        )
        rect = self.lblWidBlog.Rect
        self.lblLinkWidBlog = wx.HyperlinkCtrl(
            self,
            id = -1,
            label = u'http://www.cnblogs.com/mr-wid',
            url = u'http://www.cnblogs.com/mr-wid',
            pos = ( rect[0] + rect[2], rect[1] )
        )

        #--选项卡
        rect = self.groupBox.Rect
        self.noteBook = wx.Notebook(
            self,
            -1,
            pos = ( rect[0], rect[1] + rect[3] + 10 ),
            size=( rect[2], 170 ),
            style = wx.NB_FIXEDWIDTH
        )
        txtIntroduction = wx.TextCtrl(
            self.noteBook,
            -1,
            style = wx.MULTIPLE|wx.TE_READONLY
        )
        txtLicense = wx.TextCtrl(
            self.noteBook,
            -1,
            style = wx.MULTIPLE|wx.TE_READONLY
        )
        txtOthers = wx.TextCtrl(
            self.noteBook,
            -1,
            style = wx.MULTIPLE|wx.TE_READONLY
        )
        self.noteBook.AddPage( txtIntroduction, u"介绍" )
        self.noteBook.AddPage( txtLicense, u"协议" )
        self.noteBook.AddPage( txtOthers, u"其他" )

        #设置介绍、协议、其他文本框中的内容
        txtIntroduction.SetValue(CnblogsFan_Introduction)
        txtLicense.SetValue(CnblogsFan_License)
        txtOthers.SetValue(CnblogsFan_Others)

        #------确定按钮------
        self._btnOK = wx.Button(
            self,
            id = wx.ID_OK,
            label = u"确定",
            pos = (170, 435),
            size = (60, 30)
        )

def test():
    app = wx.PySimpleApp()
    aboutDlg = AboutDlg()
    aboutDlg.ShowModal()

if __name__ == '__main__':
    test()