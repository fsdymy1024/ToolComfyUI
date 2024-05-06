import json


def from_local_json_get_nodes(json_path):
    """
    读取本地工作流 json 文件，返回节点列表
    :param json_path:
    :return:
    """
    # nodes_json = from_github_json_load()
    local_json = json_path
    a = json.load(open(local_json, "r", encoding="utf8"))
    nodes = a.get("nodes")
    node_list = []
    for node in nodes:
        node_name = node.get("type")
        node_list.append(node_name)
    return node_list


def from_github_json_load():
    """
    从 github json 文件加载 json
    :return:
    """
    node_file = "nodeName.json"
    with open(node_file, "r", encoding="utf8") as f:
        nodes_json = json.load(f)
    return nodes_json


def get_plugin(f_node_name, f_nodes):
    """
    通过节点名称在 json 中查询对应插件项目地址，返回字符串
    :param f_node_name:
    :param f_nodes:
    :return:
    """
    data = []
    for key, value in f_nodes.items():
        element_to_find = f_node_name
        # print(value[0])
        if element_to_find in value[0]:
            txt = f"节点 {element_to_find} 在插件 {key}"
            data.append(txt)
    return data


def from_plugin_get_nodes(f_plugin, f_nodes):
    """
    根据插件项目地址查询节点列表，返回节点列表
    :param f_plugin:
    :param f_nodes:
    :return:
    """
    data = []
    for key, value in f_nodes.items():
        if f_plugin == key:
            # print(value)
            for node in value[0]:
                data.append(node)
    return data


if __name__ == "__main__":
    pass
