import re

import requests

link = input().rstrip()
#link = "http://pastebin.com/raw/hfMThaGb"
link = requests.get(link)


def get_links(linko):
    _links = []
    if linko.status_code != 200:
        print("link status code != 200!!!")
    pattern = re.compile(r'<a.+?href=["|\']{1}(?:http:\/\/|ftp:\/\/|https:\/\/)?([\w-]*[.]?[\w-]+(?:[.][\w-]+)+).*?')
    _links += pattern.findall(link.text)
    return sorted(set(_links))


links = get_links(link)
print(*links, sep='\n')