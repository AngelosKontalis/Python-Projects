import networkx as nx
from matplotlib.pyplot import *

G=nx.Graph()
G.add_nodes_from(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'])
G.add_edges_from([('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G'),('D','H'),('D','I'),('E','J'),
                  ('E','K'),('F','L'),('F','M'),('G','N'),('G','O')])
pos = {'A': (0,0), 'B': (-20, -10), 'C': (20, -10),'D':[-30,-20],'E':[-10,-20],'F':[10,-20],'G':[30,-20],
       'H': (-35,-30),'I': (-25,-30),'J': (-15,-30),'K': (-5,-30),'L': (5,-30),'M': (15,-30),'N': (25,-30),'O': (35,-30)}

visited_node=list()

def DFS_algorithm(node):
    title("→".join(visited_node))
    if node not in visited_node:
        visited_node.append(node)
        nx.draw_networkx(G,pos,nodelist=node,node_size=1000,node_color='red')
        show(block=False)
        pause(0.4)
        nx.draw_networkx(G,pos,nodelist=node,node_size=1000,node_color='green')
        show(block=False)
        pause(0.1)
        for neighbour in G[node]:
            DFS_algorithm( neighbour)

nx.draw_networkx(G,pos,node_size=1000)
DFS_algorithm('C')
pause(5)

