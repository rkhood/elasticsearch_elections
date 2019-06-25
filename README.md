# Storing election data with Elasticsearch

I wanted to play around with ES by:

- setting up an ES cluster locally
- using the ES management API

I've added some data around the [seats won](http://www.ukpolitical.info/ByYear.htm) by the Conservatives, Labour and Liberal Democrats <sup>[(1)](#LD)</sup> in all UK general elections held since 1945, and their respective [manifesto titles](https://en.wikipedia.org/wiki/List_of_Labour_Party_(UK)_general_election_manifestos).  Each data point includes:

- year of general election
- party
- seats won
- manifesto title

This is stored in an ES cluster with two nodes, with 1 shard in node-1 and 1 replica in node-2.  To run the cluster, download 2 instances of [ES](https://www.elastic.co/guide/en/elasticsearch/reference/7.1/getting-started-install.html), swap out the `config/elasticsearch.yml` files, `cd` into each ES folder's `/bin` directory and execute `./elasticsearch`.  I also wrote some scripts to interact with the ES instance to:

- add the dataset: `python -m data`
- check cluster health: `python -m health insert_port`
- count all docs: `python -m count_docs`
- retrieve all docs: `python -m retrieve`
- query all docs: e.g. `python -m query manifesto britain`
- add a doc: `python -m add_doc '{"manifesto": "Labour Labour Labour", "party": "Labour","seats": 200, "year": "2050"}'`
- delete a doc: `python -m delete_doc insert_doc_id`


Happy ES'ing!


<a name="LD">1</a>: Note, the Liberal Democrats in this dataset are an amalgamation of the Liberal Democrats (won seats from 1992 onwards), the Liberal party (won seats from 1945-1979), the Liberal Alliance (won seats from 1983-87) and the National Liberal party (won seats from 1945-66).