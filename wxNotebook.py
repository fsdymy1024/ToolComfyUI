# -*- coding: utf-8 -*-
import base64
import io
import os.path

import wx
import wx.dataview
import wx.richtext
import wx.xrc
from PIL import Image


###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ComfyUI Tool @凡意(fsdymy)", pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        if os.path.exists("wx.ico"):
            self.icon1 = wx.Icon(name="wx.ico", type=wx.BITMAP_TYPE_ICO)
            self.SetIcon(self.icon1)
        else:
            ico_base64 = r'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADblhIc25YSk9uWEpXblhIeAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANuWEh7blhKV25YS69uWEtPblhLT25YS69uWEpnblhIgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA25YSHtuWEpfblhLr25YSh9uWEhTblhKB25YSgduWEhLblhKF25YS69uWEpnblhIgAAAAAAAAAADblhIW25YSm9uWEuvblhKF25YSFAAAAAAAAAAA25YSgduWEoEAAAAAAAAAANuWEhLblhKF25YS69uWEpvblhIW25YSfNuWErHblhISAAAAAAAAAAAAAAAAAAAAANuWEoHblhKBAAAAAAAAAAAAAAAAAAAAANuWEhLblhKx25YSfNuWEn7blhJ+AAAAAAAAAAAAAAAAAAAAAAAAAADblhKB25YSgQAAAAAAAAAAAAAAAAAAAAAAAAAA25YSftuWEn7blhJ+25YSfgAAAADblhIG25YSXAAAAAAAAAAA25YSgduWEoEAAAAAAAAAAAAAAAAAAAAAAAAAANuWEn7blhJ+25YSftuWEn4AAAAA25YSHNuWEuMAAAAAAAAAANuWEoXblhKBAAAAAAAAAAAAAAAAAAAAAAAAAADblhJ+25YSftuWEn7blhJ+AAAAANuWEhzblhLj25YSKtuWEqXblhLp25YS69uWEovblhIUAAAAAAAAAAAAAAAA25YSftuWEn7blhJ+25YSfgAAAADblhI+25YS+9uWEufblhJ225YSDtuWEhjblhKV25YS69uWEnrblhIMAAAAANuWEn7blhJ+25YSftuWEqfblhKt25YS5duWErHblhLl25YSaNuWEgYAAAAAAAAAANuWEiTblhKn25YS5duWEmrblhKF25YSftuWEnjblhL/25YSkduWEgoAAAAA25YSMNuWErfblhLb25YSWNuXEgIAAAAAAAAAANuWEjLblhLN25YS+9uWEnbblhIM25YSftuWEuvblhKX25YSHAAAAAAAAAAA25YSQtuWEsnblhLN25YSRtuWEiLblhKh25YS6duWEnLblhIIAAAAAAAAAADblhIU25YSiduWEuvblhKR25YSFgAAAADblxIC25YSbNuWEv3blhLt25YSftuWEg4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADblhIW25YSj9uWEuvblhKL25YSi9uWEuvblhKL25YSFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADblhIc25YSkduWEpPblhIaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/n8AAPgfAADiRwAAjnEAAL59AAD+fwAA/n8AAPZ/AAD0PwAA858AAIPlAACc+QAAzzMAAOPPAAD4HwAA/n8AAA=='
            # 将base64编码的字符串解码为二进制数据
            image_data = base64.b64decode(ico_base64)
            # 使用BytesIO将二进制数据转为图像文件对象
            image_file = io.BytesIO(image_data)
            # 使用PIL库打开图像文件
            icon_image = Image.open(image_file)
            icon_image.save("wx.ico")
            self.icon1 = wx.Icon(name="wx.ico", type=wx.BITMAP_TYPE_ICO)
            self.SetIcon(self.icon1)
        self.SetSizeHints(wx.Size(800, 600), wx.Size(800, 600))

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_panel0 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sbSizer0 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel0, wx.ID_ANY, u"使用说明:"), wx.VERTICAL)

        self.m_staticText0 = wx.StaticText(sbSizer0.GetStaticBox(), wx.ID_ANY,
                                           u"1. 工作流查插件\n    选择工作流 json 文件，提交返回工作流依赖的插件项目地址\n2. 节点名称查询插件\n    根据节点名称 (只能是英文名称) 查询插件项目地址，可用于节点替换\n3. 插件查询节点\n    输入插件项目地址，返回插件有哪些节点\n4. Python 包查询\n    输入 ComfyUI 本地路径和 pip 包名称，返回插件依赖的 pip 版本信息",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText0.Wrap(-1)

        sbSizer0.Add(self.m_staticText0, 0, wx.ALL, 5)

        self.m_toggleBtn0 = wx.ToggleButton(sbSizer0.GetStaticBox(), wx.ID_ANY, u"同步 node 节点信息",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer0.Add(self.m_toggleBtn0, 0, wx.ALL, 5)

        self.m_staticText0 = wx.StaticText(sbSizer0.GetStaticBox(), wx.ID_ANY,
                                           u"工具运行依赖 nodeName.json 文件，打开工具时会自动更新/生成，网络异常可能会失败，可以点击上面按钮同步.",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText0.Wrap(-1)

        sbSizer0.Add(self.m_staticText0, 0, wx.ALL, 5)

        self.m_panel0.SetSizer(sbSizer0)
        self.m_panel0.Layout()
        sbSizer0.Fit(self.m_panel0)
        self.m_notebook1.AddPage(self.m_panel0, u"0. 工具说明", False)
        self.m_panel1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"选择ComfyUI工作流(JSON)：", wx.DefaultPosition,
                                           wx.Size(-1, -1), 0)
        self.m_staticText1.Wrap(-1)

        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_filePicker1 = wx.FilePickerCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.json",
                                               wx.DefaultPosition, wx.Size(-1, -1), wx.FLP_DEFAULT_STYLE)
        bSizer1.Add(self.m_filePicker1, 0, wx.ALL | wx.EXPAND, 5)

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button(self.m_panel1, wx.ID_OK)
        m_sdbSizer1.AddButton(self.m_sdbSizer1OK)
        self.m_sdbSizer1Cancel = wx.Button(self.m_panel1, wx.ID_CANCEL)
        m_sdbSizer1.AddButton(self.m_sdbSizer1Cancel)
        m_sdbSizer1.Realize()

        bSizer1.Add(m_sdbSizer1, 1, wx.ALL, 5)

        self.m_richText1 = wx.richtext.RichTextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.Size(-1, -1),
                                                    0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        self.m_richText1.SetMinSize(wx.Size(-1, 410))

        bSizer1.Add(self.m_richText1, 1, wx.ALIGN_TOP | wx.ALL | wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer1)
        self.m_panel1.Layout()
        bSizer1.Fit(self.m_panel1)
        self.m_notebook1.AddPage(self.m_panel1, u"1. 工作流查询插件", False)
        self.m_panel2 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"输入节点名称 (英文，如：PreviewImage)：",
                                           wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        bSizer2.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrl2, 0, wx.ALL | wx.EXPAND, 5)

        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button(self.m_panel2, wx.ID_OK)
        m_sdbSizer2.AddButton(self.m_sdbSizer2OK)
        self.m_sdbSizer2Cancel = wx.Button(self.m_panel2, wx.ID_CANCEL)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Cancel)
        m_sdbSizer2.Realize()

        bSizer2.Add(m_sdbSizer2, 1, wx.ALL, 5)

        self.m_richText2 = wx.richtext.RichTextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.Size(-1, -1),
                                                    0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        self.m_richText2.SetMinSize(wx.Size(-1, 410))

        bSizer2.Add(self.m_richText2, 1, wx.ALIGN_TOP | wx.ALL | wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer2)
        self.m_panel2.Layout()
        bSizer2.Fit(self.m_panel2)
        self.m_notebook1.AddPage(self.m_panel2, u"2. 节点名称查询插件", False)
        self.m_panel3 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self.m_panel3, wx.ID_ANY,
                                           u"输入插件 github 地址 (如：https://github.com/cubiq/ComfyUI_IPAdapter_plus)",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        bSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_textCtrl3, 0, wx.ALL | wx.EXPAND, 5)

        m_sdbSizer3 = wx.StdDialogButtonSizer()
        self.m_sdbSizer3OK = wx.Button(self.m_panel3, wx.ID_OK)
        m_sdbSizer3.AddButton(self.m_sdbSizer3OK)
        self.m_sdbSizer3Cancel = wx.Button(self.m_panel3, wx.ID_CANCEL)
        m_sdbSizer3.AddButton(self.m_sdbSizer3Cancel)
        m_sdbSizer3.Realize()

        bSizer3.Add(m_sdbSizer3, 1, wx.ALL, 5)

        self.m_richText3 = wx.richtext.RichTextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.Size(-1, -1),
                                                    0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        self.m_richText3.SetMinSize(wx.Size(-1, 410))

        bSizer3.Add(self.m_richText3, 1, wx.ALIGN_TOP | wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer3)
        self.m_panel3.Layout()
        bSizer3.Fit(self.m_panel3)
        self.m_notebook1.AddPage(self.m_panel3, u"3. 插件查询节点", False)
        self.m_panel4 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self.m_panel4, wx.ID_ANY, r"输入 ComfyUI 路径 (如：C:\Ai\ComfyUI)：",
                                           wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        bSizer4.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4_2 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"输入 pip 包名称 (如：transformers)：",
                                             wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText4_2.Wrap(-1)

        bSizer4.Add(self.m_staticText4_2, 0, wx.ALL, 5)

        self.m_textCtrl4_2 = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer4.Add(self.m_textCtrl4_2, 0, wx.ALL | wx.EXPAND, 5)

        m_sdbSizer4 = wx.StdDialogButtonSizer()
        self.m_sdbSizer4OK = wx.Button(self.m_panel4, wx.ID_OK)
        m_sdbSizer4.AddButton(self.m_sdbSizer4OK)
        self.m_sdbSizer4Cancel = wx.Button(self.m_panel4, wx.ID_CANCEL)
        m_sdbSizer4.AddButton(self.m_sdbSizer4Cancel)
        m_sdbSizer4.Realize()

        bSizer4.Add(m_sdbSizer4, 1, wx.ALL, 5)

        self.m_dataViewListCtrl4 = wx.dataview.DataViewListCtrl(self.m_panel4, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.DefaultSize, wx.dataview.DV_ROW_LINES)
        self.m_dataViewListCtrl4.SetMinSize(wx.Size(-1, 320))
        self.m_dataViewListCtrl4.AppendTextColumn("序号", width=100)
        self.m_dataViewListCtrl4.AppendTextColumn("插件名称", width=250)
        self.m_dataViewListCtrl4.AppendTextColumn("依赖 Python 包版本", width=300)

        bSizer4.Add(self.m_dataViewListCtrl4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel4.SetSizer(bSizer4)
        self.m_panel4.Layout()
        bSizer4.Fit(self.m_panel4)
        self.m_notebook1.AddPage(self.m_panel4, u"4. Python 包查询", True)

        bSizer.Add(self.m_notebook1, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(bSizer)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_toggleBtn0.Bind(wx.EVT_TOGGLEBUTTON, self.sync_json)
        self.m_sdbSizer1Cancel.Bind(wx.EVT_BUTTON, self.btnCancel1)
        self.m_sdbSizer1OK.Bind(wx.EVT_BUTTON, self.btnOk1)
        self.m_sdbSizer2Cancel.Bind(wx.EVT_BUTTON, self.btnCancel2)
        self.m_sdbSizer2OK.Bind(wx.EVT_BUTTON, self.btnOk2)
        self.m_sdbSizer3Cancel.Bind(wx.EVT_BUTTON, self.btnCancel3)
        self.m_sdbSizer3OK.Bind(wx.EVT_BUTTON, self.btnOk3)
        self.m_sdbSizer4Cancel.Bind(wx.EVT_BUTTON, self.btnCancel4)
        self.m_sdbSizer4OK.Bind(wx.EVT_BUTTON, self.btnOk4)
        self.m_dataViewListCtrl4.Bind(wx.dataview.EVT_DATAVIEW_COLUMN_HEADER_CLICK, self.colSort, id=wx.ID_ANY)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def sync_json(self, event):
        event.Skip()

    def btnCancel1(self, event):
        event.Skip()

    def btnOk1(self, event):
        event.Skip()

    def btnCancel2(self, event):
        event.Skip()

    def btnOk2(self, event):
        event.Skip()

    def btnCancel3(self, event):
        event.Skip()

    def btnOk3(self, event):
        event.Skip()

    def btnCancel4(self, event):
        event.Skip()

    def btnOk4(self, event):
        event.Skip()

    def colSort(self, event):
        event.Skip()
