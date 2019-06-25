'''
Retrieve health of ES cluster
'''
from elasticsearch import Elasticsearch
import sys
from formatting import CL


def get_health(port=9200):

    client = Elasticsearch([{'host': 'localhost', 'port': port}])
    health = client.cluster.health()

    for key, val in health.items():

        if key == 'status':
            if val == 'red':
                print("{} {}".format(
                    CL.BOLD + key + CL.ENDC, CL.RED + val + CL.ENDC))
            if val == 'yellow':
                print("{} {}".format(
                    CL.BOLD + key + CL.ENDC, CL.YELLOW + val + CL.ENDC))
            if val == 'green':
                print("{} {}".format(
                    CL.BOLD + key + CL.ENDC, CL.GREEN + val + CL.ENDC))
        else:
            print("{} {}".format(CL.BOLD + key + CL.ENDC, val))


if __name__ == '__main__':

    get_health(sys.argv[1])
