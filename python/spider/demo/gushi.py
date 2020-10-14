import requests
from pyquery import PyQuery as pq
from PIL import Image
import matplotlib.pyplot as plt

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}


def download_code(s):
    url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    r = s.get(url=url, headers=headers)
    html = pq(r.text)
    image_src = 'https://so.gushiwen.org/' + html.find('img#imgCode').attr('src')
    r_image = s.get(image_src, headers=headers)
    with open('code.png', 'wb') as fp:
        fp.write(r_image.content)
    img = Image.open('code.png')
    plt.figure("code")
    plt.imshow(img)
    plt.show()
    # 查找表单所需要的两个参数
    __VIEWSTATE = html.find('input#__VIEWSTATE').val()
    __VIEWSTATEGENERATOR = html.find('input#__VIEWSTATEGENERATOR').val()
    return __VIEWSTATE, __VIEWSTATEGENERATOR


def fetch_collection(r):
    html = pq(r.text)
    lines = html.find('div.sons div.cont a')
    for line in lines:
        print(line.text)


# 模拟登录
def login(view, viewg, s):
    post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
    # 提示用户输入验证码
    code = input('输入验证码=>')
    formdata = {
        '__VIEWSTATE': view,
        '__VIEWSTATEGENERATOR': viewg,
        'from': 'http://so.gushiwen.org/user/collect.aspx',
        'email': '370450848@qq.com',
        'pwd': 'essilor123',
        'code': code,
        'denglu': '登录',
    }
    return s.post(url=post_url, headers=headers, data=formdata)


def main():
    s = requests.Session()
    # 验证码
    view, viewg = download_code(s)
    lg = login(view, viewg, s)
    fetch_collection(lg)


if __name__ == '__main__':
    main()
