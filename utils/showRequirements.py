import os
from utils.utils import base_path


custom_nodes_path = os.path.join(base_path, "custom_nodes")


def show_requirements(folder_name):
    all_files = {}
    custom_nodes_list = os.listdir(folder_name)
    for custom_node in custom_nodes_list:
        if os.path.isdir(os.path.join(folder_name, custom_node)):
            if custom_node != "__pycache__":
                if os.path.exists(os.path.join(folder_name, custom_node, "requirements.txt")):
                    all_files.update({custom_node: []})
                    with open(os.path.join(folder_name, custom_node, "requirements.txt")) as req:
                        x = req.readlines()
                        # print(x)
                        for i in x:
                            if i.strip():
                                all_files[custom_node].append(i.strip())
            # print(custom_node)
    # with open(custom_nodes_path) as f:
    return all_files


if __name__ == "__main__":
    a = show_requirements(custom_nodes_path)
    # print(a)
    for k, v in a.items():
        # print(v, "***")
        print(k, " --- ", end="")
        for pip in v:
            # print(v.index(pip))
            if v.index(pip) != len(v)-1:
                print(pip, ", ", end="")
            else:
                print(pip, end="")
        print()
