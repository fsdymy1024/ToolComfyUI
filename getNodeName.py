import requests
import json


def sync_json():
    url = "https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/extension-node-map.json"
    headers = {
        'Content': "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'}

    r = requests.get(url=url, verify=False, timeout=10, headers=headers)

    if r.status_code == 200 or r.status_code == 304:
        data = r.json()
        with open("nodeName.json", "w", encoding="utf8") as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)
        return 1
    else:
        print(r.status_code)
        return 0
