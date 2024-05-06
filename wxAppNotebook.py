import os
import time

import wx
from wxNotebook import MyFrame1
from utils import from_github_json_load, from_local_json_get_nodes, get_plugin, from_plugin_get_nodes
from getNodeName import sync_json

json_path = os.path.join(os.path.dirname(__file__), "nodeName.json")
# print(json_path)
if os.path.exists(json_path):
    nodes_json = from_github_json_load()

else:
    sync_json()
    nodes_json = from_github_json_load()


class MainWin(MyFrame1):
    def btnOk1(self, event):
        if self.m_filePicker1.GetPath() == "":
            self.m_richText1.SetValue("Select a JSON file.")
        else:
            self.m_richText1.SetValue("")
            # nodes_json = from_github_json_load()
            file_path = self.m_filePicker1.GetPath()
            nodes = from_local_json_get_nodes(file_path)
            nodes = list(set(nodes))
            # self.m_richText1.SetValue((self.m_filePicker1.GetPath()))
            data = []
            for node in nodes:
                # print(node)
                txt = get_plugin(node, nodes_json)
                data.extend(txt)
            t = ""
            # print(data)
            for i in data:
                t = t + i + "\n"
            self.m_richText1.AppendText(t)

    def btnCancel1(self, event):
        self.m_filePicker1.SetPath("")
        self.m_richText1.SetValue("")

    def btnOk2(self, event):
        if self.m_textCtrl2.GetValue() == "":
            self.m_richText2.SetValue("输入节点英文名称")
            self.m_textCtrl2.SetValue("PreviewImage")
        else:
            node_name = self.m_textCtrl2.GetValue()
            txt = get_plugin(node_name, nodes_json)
            t = ""
            for i in txt:
                t = t + i + "\n"
            self.m_richText2.SetValue(t)

    def btnCancel2(self, event):
        self.m_textCtrl2.SetValue("")
        self.m_richText2.SetValue("")

    def btnOk3(self, event):
        if self.m_textCtrl3.GetValue() == "":
            self.m_richText3.SetValue("输入插件项目地址")
            self.m_textCtrl3.SetValue("https://github.com/cubiq/ComfyUI_IPAdapter_plus")
        else:
            addr = self.m_textCtrl3.GetValue()
            nodes = from_plugin_get_nodes(addr, nodes_json)
            # print(nodes)
            t = ""
            for i in nodes:
                t = t + i + "\n"
            self.m_richText3.SetValue(t)

    def btnCancel3(self, event):
        self.m_textCtrl3.SetValue("")
        self.m_richText3.SetValue("")

    def sync_json(self, event):
        self.m_staticText8.SetLabel("正在同步...")
        t = sync_json()
        print(t)
        if t:
            self.m_staticText8.SetLabel("同步成功.")
            time.sleep(1)
            self.m_staticText8.SetLabel("工具运行依赖 nodeName.json 文件，打开工具时会自动更新/生成，网络异常可能会失败，可以点击上面按钮同步.")
        else:
            self.m_staticText8.SetLabel("同步失败.")


"""
        fgSizer1.AddGrowableCol(0)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.AddGrowableRow(2)
"""

if __name__ == '__main__':
    app = wx.App()
    win = MainWin(None)
    win.Show()
    app.MainLoop()
