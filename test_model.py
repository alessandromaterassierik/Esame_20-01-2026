import networkx as nx
from model.model import Model

my_model = Model()

# DE-COMMENTARE E ADATTARE I NOMI DELLE FUNZIONI
# A QUELLE EFFETTIVAMENTE SCRITTE DURANTE L'ESAME
# PER DEBUG DEL MODEL E DELLA COSTRUZIONE DEL GRAFO
# ATTENZIONE, build_graph() RESTITUISCE UN Graph

"""
my_model.load_all_artists()
my_model.load_artists_with_min_albums(5)
G = my_model.build_graph()
print(G)
"""

# DE-COMMENTARE E ADATTARE I NOMI DELLE VARIABILI
# PER DEBUG SUL GRAFO, AD ESEMPIO, PER
# ACCEDERE ALLE INFORMAZIONI DI UN ARCO DATI I
# DUE NODI v1 e v2 RELATIVI A DUE ARTISTI CON
# id RISPETTIVAMENTE PARI A 90 (Iron Maiden) E
# 114 (Ozzy Osbourne). IN QUESTO CASO IL PESO
# (GENERI IN COMUNE DOVREBBE ESSERE PARI A 3)

"""
v1 = my_model._artists_dictionary[90]
v2 = my_model._artists_dictionary[114]
print(v1)
print(v2)
edge = G[v1][v2]
print(edge)
"""

# DE-COMMENTARE, ASSIEME AL PRIMO IMPORT, PER STAMPARE IL
# IL GRAFO USANDO matplotlib (OCCORRE ANCHE INSTALLARLO)
# NEL PROGETTO E' GIA' PRESENTE UNA IMMAGINE plot.PNG
# GENERATA PER NUMERO DI ALBUM MINIMO PARI A 5

"""
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.savefig("plot")
plt.show()
"""

