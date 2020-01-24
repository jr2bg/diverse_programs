import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

node_n = 4444#205041 #60675 #60697 #60640 #60697 #3240
int_k = 5
st_cmln = "./project {} {}".format(node_n,int_k)
os.system(st_cmln)


#####
#### k-hops
#####
#df = pd.DataFrame({ 'from':['D', 'A', 'B', 'C','A'], 'to':['A', 'D', 'A', 'E','C']})
df_kh = pd.read_csv("edges_k_hops.csv")
# Build your graph. Note that we use the DiGraph function to create the graph!
G_kh = nx.from_pandas_edgelist(df_kh, 'from', 'to', create_using=nx.DiGraph() )
# print("\n------")
# for node in G:
#     print(node)

# Make the graph
nx.draw(G_kh, with_labels=True, node_size=1500/5, alpha=1, arrows=True)

plt.show()


#####
#### Inverse path
#####
file = open("nodes_inv_path.txt", "r")
text = file.read()
file.close()
text = text.strip(" ").split(" ")
nodes_ip = [int(x) for x in text]

l_from = []
l_to = []
l_nip = len(nodes_ip)
if l_nip > 1:
    for i in range(1,l_nip):
        l_to.append(nodes_ip[l_nip - i])
        l_from.append(nodes_ip[l_nip - i - 1])

    df_invPath = pd.DataFrame({"from": l_from, "to": l_to})
    G_invPath = nx.from_pandas_edgelist(df_invPath, 'from', 'to',
                                        create_using=nx.DiGraph() )

elif l_nip == 1:
    G_invPath = nx.Graph()
    G_invPath.add_node(nodes_ip[0])

nx.draw(G_invPath, with_labels=True, node_size=1500, alpha=1, arrows=True)
plt.show()




#####
#### Independent Set
#####
file = open("ind_set.txt", "r")
text = file.read()
file.close()
text = text.strip(" ").split(" ")
ind_set = [int(x) for x in text]
if int_k > 1:

    df_indSet = pd.read_csv("edges_graph.csv")
    # Build your graph. Note that we use the DiGraph function to create the graph!
    G_indSet = nx.from_pandas_edgelist(df_indSet, 'from', 'to',
                                        create_using=nx.DiGraph())

    node_colors = []

    for node in G_indSet:
        if node in ind_set:
            node_colors.append("blue")
        else:
            node_colors.append("green")

    nx.draw(G_indSet, with_labels=True,node_color = node_colors,
            node_size=1500, alpha=1, arrows=True)
else:
    G_indSet = nx.Graph()
    G_indSet.add_node(ind_set[0])

    nx.draw(G_indSet, with_labels=True, node_color = ["blue"] ,
            node_size=1500/3, alpha=1, arrows=True)
plt.show()
