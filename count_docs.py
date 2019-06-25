'''
Count docs in ES index
'''
from elasticsearch import Elasticsearch
from formatting import CL


def count_docs(port=9200):

    client = Elasticsearch([{'host': 'localhost', 'port': port}])
    stats = client.cluster.stats()
    count = stats['indices']['docs']['count']
    print(CL.BOLD + str(count) + CL.ENDC)

    return count


if __name__ == '__main__':

    count_docs()
