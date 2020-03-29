import requests
import json

html_str = ''
with open('test.html', 'r') as f:
    rl = f.readlines()
    for text in rl:
        html_str += text


param = {"html_str": html_str}
res = requests.post('http://127.0.0.1:8090/wkhtmltopdf/bystr', param)
if res.status_code == 200:
    with open('test.pdf', 'wb') as f:
        f.write(res.content)
else:
    print(res.text)

