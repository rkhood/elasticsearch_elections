'''
Query ES index
'''
from elasticsearch import Elasticsearch
import sys
import pprint


def query_docs(term, val, port=9200):

    client = Elasticsearch([{'host': 'localhost', 'port': port}])
    res = client.search('index_1', {'query': {'match': {term: val}}})

    pprint.pprint([hit['_source'] for hit in res['hits']['hits']])

    return res


if __name__ == '__main__':

    query_docs(sys.argv[1], sys.argv[2])
