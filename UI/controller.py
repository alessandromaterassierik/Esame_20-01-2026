import flet as ft
from networkx.classes import neighbors

from UI.alert import AlertManager
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model, alert: AlertManager):
        self._view = view
        self._model = model
        self._alert = alert

    def handle_create_graph(self, e):
        try:
            int(self._view.txtNumAlbumMin.value)
        except ValueError:
            self._alert.show_alert('Metti un numero positivo')

        n_alb = int(self._view.txtNumAlbumMin.value)
        if n_alb >= 0:
            n_alb = int(n_alb)
            num_nodes, num_edges = self._model.build_graph(n_alb)
            self.populate_dd()
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f'Grafo creato: {num_nodes} nodi (artisti), {num_edges} archi'))
            self._view._page.update()

        else:
            self._alert.show_alert('Metti un numero positivo')

    def handle_connected_artists(self, e):
        # ACCESSO A ID NODO E ATTRIBUTO NODO
        n_input = int(self._view.ddArtist.value)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Artisti direttamente collegati all'artista {n_input}, {self._model._G.nodes[n_input]['name']}"))

        nodes_weight = []
        for n in self._model._G.neighbors(n_input):
                nodes_weight.append((n, self._model._G[n_input][n]['weight']))
        nodes_weight.sort(key=lambda x: x[1], reverse=True)
        for e in nodes_weight:
            self._view.txt_result.controls.append(ft.Text(f'{e[0]}, {self._model._G.nodes[e[0]]['name']} - Numero di generi in comune: {e[1]}'))
        self._view._page.update()

    def populate_dd(self):
        self._view.ddArtist.options.clear()
        for g in self._model._G.nodes:
            name = self._model._G.nodes[g]['name']
            self._view.ddArtist.options.append(ft.dropdown.Option(key = int(g), text= name))
        self._view._page.update()

    def ricerca_cammino(self, e):
        try:
            int(self._view.txtMinDuration.value)
        except ValueError:
            self._alert.show_alert('Metti un numero positivo')
        try:
            int(self._view.txtMaxArtists.value)
        except ValueError:
            self._alert.show_alert('Metti un numero positivo')
        input_duration = int(self._view.txtMinDuration.value)
        input_max_artists = int(self._view.txtMaxArtists.value)
        if input_duration <= 0:#and input_max_artists > 1 or input_max_artists <= len(self._model._G.nodes):
            self._alert.show_alert('Metti un numero positivo')
        elif input_max_artists <=0 or input_max_artists >= len(self._model._G.nodes):
            self._alert.show_alert('Metti un numero positivo tra 1 e il numero di artisti')
        else:
            n_input = int(self._view.ddArtist.value)
            n_alb = int(self._view.txtNumAlbumMin.value)
            sol_ott , d_sol = self._model.search_path(n_input, input_duration, input_max_artists, n_alb)
            print(sol_ott)
            print(d_sol)
