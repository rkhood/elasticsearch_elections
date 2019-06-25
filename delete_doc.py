'''
Delete doc from ES index
'''
from elasticsearch import Elasticsearch
import sys
from formatting import CL


def delete_doc(doc_id, port=9200):

    client = Elasticsearch([{'host': 'localhost', 'port': port}])
    res = client.delete(index='index_1', doc_type='doc', id=doc_id)
    print('{} {}'.format(CL.RED + 'Doc deleted' + CL.ENDC, doc_id))


if __name__ == '__main__':

    delete_doc(sys.argv[1])
