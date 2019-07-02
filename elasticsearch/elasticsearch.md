GET 47.100.117.15:9200/_cat/health?v

查看全部index
GET /_cat/indices?v

create index
PUT /customer?pretty

删除
PUT /customer
PUT /customer/doc/1
{
  "name": "John Doe"
}
GET /customer/doc/1
DELETE /customer
DELETE /customer/doc/2?pretty

更新
POST /customer/doc/1/_update?pretty
{
  "doc": { "name": "Jane Doe", "age": 20 }
}

批处理
POST /customer/doc/_bulk?pretty
{"index":{"_id":"1"}}
{"name": "John Doe" }（key,value需置一行）
{"index":{"_id":"2"}}
{"name": "Jane Doe" }
（空一行）


**SEARCH API**

GET /customer/_search?q=*&sort=account_number:asc&pretty

GET /customer/_search

排序
{
  "query": { "match_all": {} },
  "sort": {  "age": "desc" },
}

显示字段
{
  "query": { "match_all": {} },
  "_source": ["age", "name"]
}

条件
{
  "query": { "match": {"age":10} },
}

包含，类似like
{
  "query": { "match_phrase": {"name":"John"} }
}

布尔and
{
  "query": {
    "bool": {
      "must": [
        { "match": { "age": "10" } },
        { "match_phrase": { "name": "John" } }
      ]
    }
  }
}

布尔or
{
  "query": {
    "bool": {
      "should": [
        { "match": { "age": "29" } },
        { "match_phrase": { "name": "John" } }
      ]
    }
  }
}

布尔note
{
  "query": {
    "bool": {
      "must_not": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}

mixed
{
  "query": {
    "bool": {
      "must": [
        { "match": { "age": "40" } }
      ],
      "must_not": [
        { "match": { "state": "ID" } }
      ]
    }
  }
}

过滤。gte大于等于，lte小于等于
{
    "query": {
        "bool": {
            "must": {
                "match_all": {}
            },
            "filter": {
                "range": {
                    "age": {
                        "gte": 9,
                        "lte": 30
                    }
                }
            }
        }
    }
}

聚合
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "name.keyword"
      }
    }
  }
}

聚合求avg
{
    "size": 0,
    "aggs": {
        "group_by_state": {
            "terms": {
                "field": "name.keyword"
            },
            "aggs": {
                "age_avg": {
                    "avg": {
                        "field": "age"
                    }
                }
            }
        }
    }
}
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "name.keyword",
        "order": {
          "age_avg": "desc"
        }
      },
      "aggs": {
        "age_avg": {
          "avg": {
            "field": "age"
          }
        }
      }
    }
  }
}
