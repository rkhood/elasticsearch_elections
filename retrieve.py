'''
Query all docs in ES index
'''
from elasticsearch import Elasticsearch
from count_docs import count_docs


def retrieve_docs(port=9200):

    client = Elasticsearch([{'host': 'localhost', 'port': port}])
    count = count_docs(port=port)
    res = client.search('index_1', {"size": count, 'query': {'match_all': {}}})
    print(res)

    return res


if __name__ == '__main__':

    retrieve_docs()
