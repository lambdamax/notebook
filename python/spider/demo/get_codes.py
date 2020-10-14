import requests
from pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
r = requests.get(url=url, headers=headers)
html = pq(r.text)
image_src = 'https://so.gushiwen.org/' + html.find('img#imgCode').attr('src')
for i in range(0, 50):
    r_image = requests.get(image_src, headers=headers)
    with open('codes/code%s.png' % i, 'wb') as fp:
        fp.write(r_image.content)
