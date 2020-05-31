import jieba
import jieba.analyse
from elasticsearch import Elasticsearch

es = Elasticsearch(['172.29.21.169'], http_auth=('elastic', 'elastic'), port=9200)
response = es.search(index='essilor_product_comments',
                     body={"_source": "comment", "query": {"match_all": {}}, "size": 600})

keywords = []

for hit in response['hits']['hits']:
    # print(hit['_source'])
    comment = hit['_source']['comment']
    # 基于TextRank算法的关键词抽取
    for word in jieba.analyse.textrank(comment, topK=20, withWeight=False, allowPOS=('vn', 'a', 'ad')):
        keywords.append(word)

for word in keywords:
    print(word)
    es.index(index="essilor_product_comments_keyworks2", body=dict(word=word))
