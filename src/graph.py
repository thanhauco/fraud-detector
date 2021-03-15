import networkx as nx
G = nx.Graph()
def add_tx(user_id, location):
    G.add_edge(user_id, location)
    if nx.degree(G, user_id) > 5: return True
    return False