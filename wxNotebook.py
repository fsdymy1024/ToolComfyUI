# -*- coding: utf-8 -*-
import base64
import io

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext
from PIL import Image


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ComfyUI Tool", pos=wx.DefaultPosition,
                          size=wx.Size(700, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        ico_base64 = r'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADblhIc25YSk9uWEpXblhIeAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANuWEh7blhKV25YS69uWEtPblhLT25YS69uWEpnblhIgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA25YSHtuWEpfblhLr25YSh9uWEhTblhKB25YSgduWEhLblhKF25YS69uWEpnblhIgAAAAAAAAAADblhIW25YSm9uWEuvblhKF25YSFAAAAAAAAAAA25YSgduWEoEAAAAAAAAAANuWEhLblhKF25YS69uWEpvblhIW25YSfNuWErHblhISAAAAAAAAAAAAAAAAAAAAANuWEoHblhKBAAAAAAAAAAAAAAAAAAAAANuWEhLblhKx25YSfNuWEn7blhJ+AAAAAAAAAAAAAAAAAAAAAAAAAADblhKB25YSgQAAAAAAAAAAAAAAAAAAAAAAAAAA25YSftuWEn7blhJ+25YSfgAAAADblhIG25YSXAAAAAAAAAAA25YSgduWEoEAAAAAAAAAAAAAAAAAAAAAAAAAANuWEn7blhJ+25YSftuWEn4AAAAA25YSHNuWEuMAAAAAAAAAANuWEoXblhKBAAAAAAAAAAAAAAAAAAAAAAAAAADblhJ+25YSftuWEn7blhJ+AAAAANuWEhzblhLj25YSKtuWEqXblhLp25YS69uWEovblhIUAAAAAAAAAAAAAAAA25YSftuWEn7blhJ+25YSfgAAAADblhI+25YS+9uWEufblhJ225YSDtuWEhjblhKV25YS69uWEnrblhIMAAAAANuWEn7blhJ+25YSftuWEqfblhKt25YS5duWErHblhLl25YSaNuWEgYAAAAAAAAAANuWEiTblhKn25YS5duWEmrblhKF25YSftuWEnjblhL/25YSkduWEgoAAAAA25YSMNuWErfblhLb25YSWNuXEgIAAAAAAAAAANuWEjLblhLN25YS+9uWEnbblhIM25YSftuWEuvblhKX25YSHAAAAAAAAAAA25YSQtuWEsnblhLN25YSRtuWEiLblhKh25YS6duWEnLblhIIAAAAAAAAAADblhIU25YSiduWEuvblhKR25YSFgAAAADblxIC25YSbNuWEv3blhLt25YSftuWEg4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADblhIW25YSj9uWEuvblhKL25YSi9uWEuvblhKL25YSFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADblhIc25YSkduWEpPblhIaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/n8AAPgfAADiRwAAjnEAAL59AAD+fwAA/n8AAPZ/AAD0PwAA858AAIPlAACc+QAAzzMAAOPPAAD4HwAA/n8AAA=='
        # 将base64编码的字符串解码为二进制数据
        image_data = base64.b64decode(ico_base64)
        # 使用BytesIO将二进制数据转为图像文件对象
        image_file = io.BytesIO(image_data)
        # 使用PIL库打开图像文件
        icon_image = Image.open(image_file)
        icon_image.save("wx1.ico")

        self.icon1 = wx.Icon(name="wx1.ico", type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon1)
        self.SetSizeHints(wx.Size(700, 500), wx.Size(700, 500))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_panel1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"选择ComfyUI工作流(JSON)：", wx.DefaultPosition,
                                           wx.Size(-1, -1), 0)
        self.m_staticText1.Wrap(-1)

        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_filePicker1 = wx.FilePickerCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.json",
                                               wx.DefaultPosition, wx.Size(-1, -1), wx.FLP_DEFAULT_STYLE)
        bSizer2.Add(self.m_filePicker1, 0, wx.ALL | wx.EXPAND, 5)

        m_sdbSizer4 = wx.StdDialogButtonSizer()
        self.m_sdbSizer4OK = wx.Button(self.m_panel1, wx.ID_OK)
        m_sdbSizer4.AddButton(self.m_sdbSizer4OK)
        self.m_sdbSizer4Cancel = wx.Button(self.m_panel1, wx.ID_CANCEL)
        m_sdbSizer4.AddButton(self.m_sdbSizer4Cancel)
        m_sdbSizer4.Realize();

        bSizer2.Add(m_sdbSizer4, 1, wx.ALL, 5)

        self.m_richText1 = wx.richtext.RichTextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.Size(-1, -1),
                                                    0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        self.m_richText1.SetMinSize(wx.Size(-1, 310))

        bSizer2.Add(self.m_richText1, 1, wx.ALIGN_TOP | wx.ALL | wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        self.m_notebook1.AddPage(self.m_panel1, u"1. 工作流查询插件", True)
        self.m_panel2 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"输入节点名称(英文)：", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        bSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_textCtrl2, 0, wx.ALL | wx.EXPAND, 5)

        m_sdbSizer6 = wx.StdDialogButtonSizer()
        self.m_sdbSizer6OK = wx.Button(self.m_panel2, wx.ID_OK)
        m_sdbSizer6.AddButton(self.m_sdbSizer6OK)
        self.m_sdbSizer6Cancel = wx.Button(self.m_panel2, wx.ID_CANCEL)
        m_sdbSizer6.AddButton(self.m_sdbSizer6Cancel)
        m_sdbSizer6.Realize();

        bSizer3.Add(m_sdbSizer6, 1, wx.ALL, 5)

        self.m_richText2 = wx.richtext.RichTextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.Size(-1, -1),
                                                    0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        self.m_richText2.SetMinSize(wx.Size(-1, 310))

        bSizer3.Add(self.m_richText2, 1, wx.ALIGN_TOP | wx.ALL | wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        self.m_notebook1.AddPage(self.m_panel2, u"2. 节点名称查询插件", False)
        self.m_panel3 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self.m_panel3, wx.ID_ANY,
                                           u"输入插件 github 地址 (如：https://github.com/cubiq/ComfyUI_IPAdapter_plus)",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        bSizer4.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl3, 0, wx.ALL | wx.EXPAND, 5)

        m_sdbSizer5 = wx.StdDialogButtonSizer()
        self.m_sdbSizer5OK = wx.Button(self.m_panel3, wx.ID_OK)
        m_sdbSizer5.AddButton(self.m_sdbSizer5OK)
        self.m_sdbSizer5Cancel = wx.Button(self.m_panel3, wx.ID_CANCEL)
        m_sdbSizer5.AddButton(self.m_sdbSizer5Cancel)
        m_sdbSizer5.Realize();

        bSizer4.Add(m_sdbSizer5, 1, wx.ALL, 5)

        self.m_richText3 = wx.richtext.RichTextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.Size(-1, -1),
                                                    0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        self.m_richText3.SetMinSize(wx.Size(-1, 310))

        bSizer4.Add(self.m_richText3, 1, wx.ALIGN_TOP | wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        self.m_notebook1.AddPage(self.m_panel3, u"3. 插件查询节点", False)
        self.m_panel4 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel4, wx.ID_ANY, u"使用说明:"), wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY,
                                           u"1. 工作流查插件\n    选择工作流 json 文件，提交返回工作流依赖的插件项目地址\n2. 节点名称查询插件\n    根据节点名称 (只能是英文名称) 查询插件项目地址，可用于节点替换\n3. 插件查询节点\n    输入插件项目地址，返回插件有哪些节点",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        sbSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_toggleBtn1 = wx.ToggleButton(sbSizer1.GetStaticBox(), wx.ID_ANY, u"同步 node 节点信息",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer1.Add(self.m_toggleBtn1, 0, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY,
                                           u"工具运行依赖 nodeName.json 文件，打开工具时会自动更新/生成，网络异常可能会失败，可以点击上面按钮同步.",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        sbSizer1.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_panel4.SetSizer(sbSizer1)
        self.m_panel4.Layout()
        sbSizer1.Fit(self.m_panel4)
        self.m_notebook1.AddPage(self.m_panel4, u"0. 工具说明", False)

        bSizer1.Add(self.m_notebook1, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_sdbSizer4Cancel.Bind(wx.EVT_BUTTON, self.btnCancel1)
        self.m_sdbSizer4OK.Bind(wx.EVT_BUTTON, self.btnOk1)
        self.m_sdbSizer6Cancel.Bind(wx.EVT_BUTTON, self.btnCancel2)
        self.m_sdbSizer6OK.Bind(wx.EVT_BUTTON, self.btnOk2)
        self.m_sdbSizer5Cancel.Bind(wx.EVT_BUTTON, self.btnCancel3)
        self.m_sdbSizer5OK.Bind(wx.EVT_BUTTON, self.btnOk3)
        self.m_toggleBtn1.Bind(wx.EVT_TOGGLEBUTTON, self.sync_json)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
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

    def sync_json(self, event):
        event.Skip()
