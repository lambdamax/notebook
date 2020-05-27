import requests
from pyquery import PyQuery as pq

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'cookie': 'tk_trace=1; cna=vOPwFjpfdVoCATuUSATQbyVt; t=d74043233d8354e794462de71577f3a4; _tb_token_=eee7b03fbd3dd; cookie2=16d3cc8a67038bd6b49ae27320922e84; pnm_cku822=; dnk=%5Cu59AE%5Cu9732%5Cu827E%5Cu9732%5Cu675C; uc1=pas=0&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie21=VFC%2FuZ9ajCWYhIooqbUi6Q%3D%3D&cookie14=UoTV7NMV3i1goA%3D%3D&existShop=true; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&nk2=pxV3%2BhWFgxT3mg%3D%3D&vt3=F8dBxGettN%2FNdXwvEzc%3D&id2=Vv7JF5SCJvko; tracknick=%5Cu59AE%5Cu9732%5Cu827E%5Cu9732%5Cu675C; _l_g_=Ug%3D%3D; uc4=id4=0%40VHj1uU0SMb6jHfd6GLtS12aTpfQ%3D&nk4=0%40pSOCHb9e3Po%2Flw7ptmKGN1ktVktn; unb=500265115; lgc=%5Cu59AE%5Cu9732%5Cu827E%5Cu9732%5Cu675C; cookie1=WqPyBlcSKNFwXegVIKsIopIXnK9itbGTcSeJT%2BkDkQs%3D; login=true; cookie17=Vv7JF5SCJvko; _nk_=%5Cu59AE%5Cu9732%5Cu827E%5Cu9732%5Cu675C; sgcookie=EiD%2B9MeK41O5hYCCfLn2o; sg=%E6%9D%9C56; csg=870b4c83; cq=ccp%3D0; l=eB_vXwluQD-md4F3BOfZnurza779sIRAguPzaNbMiOCP_b5p5BdlWZAedQ89CnGVh6ckR35QyF6TBeYBqhDc7odkShlCxMkmn; isg=BObmT-m7hL8_MFAbDqQpPEfRN1xoxyqBDPKIktCP0YnkU4ZtOFMekKEtq09feyKZ',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'referer': 'https://essilor.tmall.com/search.htm?spm=a1z10.3-b-s.w5001-21031911263.4.ae9237b0ya9GjO&scene=taobao_shop'
}

url = 'https://essilor.tmall.com/i/asynSearch.htm?_ksTS=1590563659937_92&callback=jsonp93&mid=w-20537127107-0&wid=20537127107&path=/search.htm&search=y&spm=a1z10.3-b-s.w5001-21031911263.4.ae9237b0ya9GjO&scene=taobao_shop'

r = requests.get(url=url, headers=headers)
body = r.text[15:-8].replace('\\"', '"')
products = []
doc = pq(body)
items = doc('div.J_TItems div.item5line1').items()
for item in items:
    for i in item('dd.detail').items():
        name = i('a.item-name').text()
        price = i('div.attribute div.cprice-area span.c-price').text()
        sale_num = i('div.attribute div.sale-area span.sale-num').text()
        product = dict(name=name, price=float(price), sale_num=int(sale_num))
        print(product)
        products.append(product)
print(len(products))
