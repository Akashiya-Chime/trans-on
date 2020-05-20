import requests
import re

with open('D:/图/icon/GitHub_Long.png', 'rb') as f:
    png = f.read()


url = 'https://steelsoft.site/ocr/ocr_c.php'
headers = {
    'Cache-Control': 'max-age=0',
    'Origin': 'https://steelsoft.site',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-User': '?1',
    'Referer': 'https://steelsoft.site/ocr/ocr_c.php',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
f = {"max_file_size": (None, 100000000),
     "language": (None, 1),
     "a": (None, None),
     "file": ("GitHub_Long.png", open("D:/图/icon/GitHub_Long.png", "rb"), "image/png")}

r = requests.post(url, headers=headers, files=f, verify=False)
# print(r.text)

gettext = re.findall(r'<p><textarea name="a".+/p>', r.text)
ok = gettext[0]
print(ok[56:-15])
