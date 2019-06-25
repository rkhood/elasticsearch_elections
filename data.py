'''
Load original dataset to ES index
'''
import pandas as pd
from elasticsearch import Elasticsearch


def read_data(f):
    return pd.read_csv(f, index_col='Party', keep_default_na=False)


def to_ES(votes, mans, client):

    for i in votes:
        for j in votes.index:
            doc = {
                    "year": i,
                    "party": j,
                    "seats": votes[i][j],
                    "manifesto": mans[i][j],
            }
            res = client.index(index='index_1', doc_type='doc', body=doc)


if __name__ == '__main__':

    vote_data = read_data('general_election_results.csv')
    manifesto_data = read_data('manifesto_titles.csv')

    client = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    to_ES(vote_data, manifesto_data, client)
