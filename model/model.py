import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self._nodes = []
        self.id_map = {}
        self._edges = []
        self.albums = []

    def load_album(self, durata):
        self.albums = DAO.get_album_nodes(durata)
        return self.albums


    def build_graph(self, durata):
        self.G.clear()

        # nodi
        self._nodes = DAO.get_album_nodes(durata)
        self.G.add_nodes_from(self._nodes)

        # mappa {id --> oggetto }
        for n in self._nodes:
            self.id_map[n.id] = n

        #archi
        self._edges = DAO.get_edges(durata)
        for n1, n2 in self._edges:
            a1 = self.id_map[n1.id]
            a2 = self.id_map[n2.id]
            self.G.add_edge(a1, a2)

        print(f'Nodi: {self.G.number_of_nodes()}, archi: {self.G.number_of_edges()}')
        return self.G

    def get_graph_details(self):
        return self.G.number_of_nodes(), self.G.number_of_edges()