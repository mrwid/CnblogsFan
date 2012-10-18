#!/usr/bin/python
#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        CnblogsFan_FilterDlg.py
# Purpose:
#
# Author:      Mr.Wid
#
# Created:     18-10-2012
# Copyright:   (c) Mr.Wid 2012
# Licence:     GNU GPL
#-------------------------------------------------------------------------------

import wx
import time

class FilterDlg(wx.Dialog):
    def __init__( self, parent = None ):
        wx.Dialog.__init__(
            self,
            parent = parent,
            title = u'过滤设置',
            size = (500, 400)
        )
        #-----感兴趣的关键词-----
        rect = self.GetClientRect()
        #--静态库框
        self.groupKeyWordBox = wx.StaticBox(
            self,
            label = u'关键词检索(可选)',
            pos = ( rect[0] + 20 , rect[1] + 20 ),
            size = ( rect[2] - 40, rect[0] + 100 ),
        )
        #--标签提示
        rect = self.groupKeyWordBox.Rect
        self.lblKeyWord = wx.StaticText(
            self,
            label = u'感兴趣的关键词:',
            pos = ( rect[0] + 30, rect[1] + 30 )
        )
        #--关键词输入文本框
        rect = self.lblKeyWord.Rect
        self.txtKeyWord = wx.TextCtrl(
            self,
            size = ( 300, -1 ),
            pos = ( rect[0] + rect[2] + 10, rect[1] - 3 ),
            value = u'关键词之间用空格隔开',
        )
        self.tipKeyWordValue = True
        self.txtKeyWord.Bind( wx.EVT_LEFT_DOWN, self.OnClearTipText )
        #--检索方式选择单选组
        rect = self.groupKeyWordBox.Rect
        self.rdoboxKeyMode = wx.RadioBox(
            self,
            choices = [ u'仅检索标题', u'全文检索' ],
            style = wx.RA_HORIZONTAL,
        )
        self.rdoboxKeyMode.Position = (
            rect[0] + (rect[2] - self.rdoboxKeyMode.Rect[2]) / 2 ,
            rect[1] + (rect[3] - self.rdoboxKeyMode.Rect[3]) / 2 + 20
        )

        #-----时间过滤-----
        rect = self.groupKeyWordBox.Rect
        self.groupTimeBox = wx.StaticBox(
            self,
            label = u'允许采集的时间范围(可选)',
            pos = ( rect[0] , rect[1] + rect[3] + 20 ),
            size = ( rect[2], rect[0] + 50 ),
        )
         #-----起始日期下拉选单
        #--起始年份
        year = []
        for i in range(int( time.localtime()[0]), 2002 , -1 ):
            year.append( str(i) )
        rect = self.groupTimeBox.Rect
        self.cboStartYear = wx.ComboBox(
            self,
            value = u'年',
            pos = ( rect[0] + 30, rect[1] + 30 ),
            choices = year
        )
        #--起始月份
        month = []
        for i in range( 1, 13 ):
            month.append( str(i) )
        rect = self.cboStartYear.Rect
        self.cboStartMonth = wx.ComboBox(
            self,
            value = u'月',
            pos = ( rect[0] + rect[2] + 10, rect[1] ),
            choices = month
        )
        #--起始天数
        rect = self.cboStartMonth.Rect
        self.cboStartDay = wx.ComboBox(
            self,
            value = u'日',
            pos = ( rect[0] + rect[2] + 10, rect[1] ),
            size = ( rect[2], rect[3] ),
        )
        self.cboStartMonth.Bind( wx.EVT_COMBOBOX, self.OnShowStartDay )
        self.cboStartYear.Bind( wx.EVT_COMBOBOX, self.OnShowStartDay )
        #--标签
        rect = self.cboStartDay.Rect
        wx.StaticText(
            self, label = u'至',
            pos = ( rect[0] + rect[2] + 15, rect[1] + 3 )
        )
        #-----截止日期下拉选单
        #--结束年份
        year = []
        for i in range(int( time.localtime()[0]), 2002 , -1 ):
            year.append( str(i) )
        rect = self.groupTimeBox.Rect
        self.cboEndYear = wx.ComboBox(
            self,
            value = u'年',
            pos = ( rect[0] + 240, rect[1] + 30 ),
            choices = year
        )
        #--结束月份
        month = []
        for i in range( 1, 13 ):
            month.append( str(i) )
        rect = self.cboEndYear.Rect
        self.cboEndMonth = wx.ComboBox(
            self,
            value = u'月',
            pos = ( rect[0] + rect[2] + 10, rect[1] ),
            choices = month
        )
        #--结束天数
        rect = self.cboEndMonth.Rect
        self.cboEndDay = wx.ComboBox(
            self,
            value = u'日',
            pos = ( rect[0] + rect[2] + 10, rect[1] ),
            size = ( rect[2], rect[3] ),
        )
        self.cboEndMonth.Bind( wx.EVT_COMBOBOX, self.OnShowEndDay )
        self.cboEndYear.Bind( wx.EVT_COMBOBOX, self.OnShowEndDay )

        #-----允许采集的最短内容长度
        rect = self.groupTimeBox.Rect
        self.groupLeastBox = wx.StaticBox(
            self,
            label = u'允许采集的随笔最短字数(可选)',
            pos = ( rect[0] , rect[1] + rect[3] + 20 ),
            size = ( rect[2], rect[3] ),
        )
        #--建议一个滑块
        rect = self.groupLeastBox.Rect
        self.sliderLeastWord = wx.Slider(
            self,
            value = 0,
            minValue = 0,
            maxValue = 5000,
            pos = ( rect[0] + 20, rect[1] + 20 ),
            size = ( 410, -1 ),
            style = wx.SL_HORIZONTAL |  wx.SL_LABELS
        )
        #-----开始采集按钮-----
        rect = self.GetClientRect()
        self.btnStart = wx.Button(
            self,
            label = u'开始采集',
            size = ( 80, 40 ),
            pos = (  (rect[2] - 80 ) / 2 , rect[3] - 50 )
        )


    #-----事件响应方法------
    #--清空文本框提示文字
    def OnClearTipText( self, evt ):
        self.txtKeyWord.SetFocus()
        if self.tipKeyWordValue:
            self.txtKeyWord.SetValue(u'')
            self.tipKeyWordValue = False

    #--计算结束下拉选单结束日期"日"的天数
    def OnShowStartDay( self, evt ):
        try:
            year = int( self.cboStartYear.GetLabel() )
            month = self.cboStartMonth.GetLabel()
        except:
            return
        day = 31
        while day:
            try:
                time.strptime('%s-%s-%s'%(year, month, str(day)), '%Y-%m-%d')
                self.lstDay = [ str(i) for i in range(1, day + 1) ]
                self.cboStartDay.SetItems(self.lstDay)
                self.cboStartDay.SetLabel( u'日' )
                break
            except:
                day -= 1

    #--计算结束下拉选单结束日期"日"的天数
    def OnShowEndDay( self, evt ):
        try:
            year = int( self.cboEndYear.GetLabel() )
            month = self.cboEndMonth.GetLabel()
        except:
            return
        day = 31
        while day:
            try:
                time.strptime('%s-%s-%s'%(year, month, str(day)), '%Y-%m-%d')
                self.lstDay = [ str(i) for i in range(1, day + 1) ]
                self.cboEndDay.SetItems(self.lstDay)
                self.cboEndDay.SetLabel( u'日' )
                break
            except:
                day -= 1


def test():
    app = wx.PySimpleApp()
    dlg = FilterDlg()
    dlg.ShowModal()

if __name__ == '__main__':
    test()
