'''
Add doc to ES index
'''
from elasticsearch import Elasticsearch
import sys
from formatting import CL
import json


def add_doc(doc, port=9200):

    client = Elasticsearch([{'host': 'localhost', 'port': port}])
    res = client.index(index='index_1', doc_type='doc', body=doc)

    try:
        print('{} {}'.format(CL.GREEN + 'Doc added' + CL.ENDC, res['_id']))
    except:
        print(CL.RED + 'Unable to add doc, indexing failed' + CL.ENDC)


if __name__ == '__main__':

    add_doc(json.loads(sys.argv[1]))
