import networkx as nx
from networkx.classes import neighbors

from database.dao import DAO

class Model:
    def __init__(self):
        self._G = nx.DiGraph()
        self._G_path= nx.DiGraph()
        self._artists_list = []
        self._album_artists = []
        self.load_all_artists()

    def load_all_artists(self):#[{'id': 1, 'name': 'AC/DC'}, {'id': 2, 'name': 'Accept'}
        self._artists_list = DAO.get_all_artists()

    def load_artists_with_min_albums(self, min_albums):#[{'art1': 2, 'art2': 1, 'generi_com': 1}, {'art1': 8, 'art2': 1, 'generi_com': 1},
        self._album_artists = DAO.get_num_albums(min_albums)

    def build_graph(self, min_albums):
        self.load_artists_with_min_albums(min_albums)
        for p in self._album_artists:
            self._G.add_node(p['art1'], name=p['name1'])
            self._G.add_node(p['art2'], name=p['name2'])
            self._G.add_weighted_edges_from([(p['art1'], p['art2'], p['generi_com'])])
        return len(self._G.nodes), len(self._G.edges)

    def search_path(self, a1, d_min, n_art, n_alb):
        #cammino peso max = n_art
        #nodo iniziale = a1
        #artisti con almeno una canzone d_min
        self._album_artists = DAO.get_albums_filtered(n_alb, d_min)
        for p in self._album_artists:
            self._G_path.add_node(p['art1'], name=p['name1'])
            self._G_path.add_node(p['art2'], name=p['name2'])
            self._G_path.add_weighted_edges_from([(p['art1'], p['art2'], p['generi_com'])])

        sol_part = [a1]
        self.sol_ott = sol_part
        self.d_fin = 0
        self.ricorsione(n_input=a1, start_index=0, sol_part=[a1], d_cur=0, max_d=n_art)

        return self.sol_ott, self.d_fin

    def ricorsione(self, n_input, start_index, sol_part, d_cur, max_d):
        #update
        if len(sol_part) > len(self.sol_ott):
            self.sol_ott = sol_part.copy()
            self.d_fin = d_cur

        # end
        if start_index == max_d:
            return

        # ciclo
        for i in range(start_index, max_d):
            for n in self._G_path.neighbors(n_input):
                d_n = int(self._G_path[n_input][n]['weight'])
                if len(sol_part) <= max_d:
                    sol_part.append(n)
                    self.ricorsione(n, start_index + 1, sol_part, d_cur + d_n, max_d)
                    sol_part.pop()

