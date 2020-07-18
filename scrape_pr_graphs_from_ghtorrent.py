import MySQLdb
import networkx as nx
import pickle
import random
import math

# connect to ghtorrent db dump
db=MySQLdb.connect(
                 host="127.0.0.1", 
                 user="root", 
                 passwd="enterenter"
               )
cursor = db.cursor()
cursor.execute("use ghtorrent_restore")

fails=0

#File with all project ids that were no forks of other projects (more than 30 million)
# These ids were obtained in a separate database query
idrange=pickle.load(open("nofork_ids.p", "rb"))
print("got id_list. length: ", len(idrange))

def chunkify(lst,n):
    return [lst[i::n] for i in range(n)]

chunk_no=100
idlists=chunkify(idrange,chunk_no)

for li_n,li in enumerate(idlists[:50]):
    with open("path/to/folder/pickle_graphs_all_randSample_noFork_6months_chunk"+str(li_n)+".gpickle", "wb") as f:
        for i,n_id in enumerate(li):
            try: 
                sql_str2="""
                select prh2.actor_id, prh1.actor_id
                  from pull_requests pr, pull_request_history prh1, pull_request_history prh2
                  where pr.base_repo_id = %s
                    and prh1.pull_request_id = pr.id
                    and prh2.pull_request_id = pr.id
                    and prh1.action = 'opened'
                    and prh2.action = 'merged'
                    and prh2.created_at BETWEEN date('2016-09-01') AND date("2017-03-01")
                """%(n_id)
                
                
                cursor.execute(sql_str2)
                merge_pairs=cursor.fetchall()

                if len(merge_pairs) > 0:
                    G = nx.DiGraph(id=n_id)

                    for p in merge_pairs:
                        if G.has_edge(p[1], p[0]):
                            # we added this one before, just increase the weight by one
                            G[p[1]][p[0]]['weight'] += 1
                        else:
                            # new edge. add with weight=1
                            G.add_edge(p[1], p[0], weight=1) 
                    nx.write_gpickle(G, f)
                if i%100==0:
                    print(li_n,i)

            except:
                print("fail")
                fails+=1
                if fails%10==0:
                    print("no of fails: ", fails)
                pass

