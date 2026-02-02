import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        durata = int(self._view.txt_durata.value)

        self._model.build_graph(durata)
        album = self._model.load_album(durata)
        for a in album:
            self._view.dd_album.options.append(ft.dropdown.Option(key = a.id, text = a))

        nodi,archi = self._model.get_graph_details()
        self._view.lista_visualizzazione_1.clean()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f'Grafo creato: {nodi} album, {archi} archi'))

        self._view.update()
        # TODO

    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""

        # TODO

    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        # TODO

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO