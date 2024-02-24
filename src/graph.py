import networkx as nx
from networkx import Graph
import matplotlib.pyplot as plt
from random import randint
from typing import List


class GraphVisualization:
    def __init__(self) -> None:
        self.graph: Graph = None 
        self.position = None

    
    def __init_new_graph(self):
        self.graph = nx.Graph()

    def __add_graph_edges(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i != j:
                    self.graph.add_edge(i, j, weight=matrix[i][j])
        self.position = nx.spring_layout(self.graph)

    def __display_graph(self):
        plt.title('Shortest Path for Traveling Salesman Problem')
        plt.show()

    def __set_edges_labels(self, distan):
         # for output edge labels of graph
        edge_labels = {(i,j): distan[i][j] for i in range(len(distan)) for j in range(len(distan)) if i != j}
        nx.draw_networkx_edge_labels(self.graph, self.position, edge_labels=edge_labels, label_pos=0.3, font_size=10)

    def draw(self, matrix, shortest_path):
        self.__init_new_graph()
        self.__add_graph_edges(matrix)

        edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
        nx.draw_networkx_edges(self.graph, 
                               self.position, 
                               edgelist=edges, 
                               edge_color='r', 
                               width=2, 
                               arrows=True, 
                               arrowstyle='->, head_width=0.5, head_length=0.8')

        self.__set_edges_labels(matrix)

        nx.draw(self.graph, 
                self.position, 
                with_labels=True, 
                node_color='lightblue', 
                node_size=400, font_weight='bold', 
                font_size=10, 
                edge_color='gray')

        self.__display_graph()


class GraphGeneration:
    def __init__(self, num_of_vertex: int, low_limit: int, upper_limit: int) -> None:
        self.num_of_vertex = num_of_vertex
        self.low_limit = low_limit
        self.upper_limit = upper_limit

    def generate_matrix(self) -> List[List[int]]:
        matrix = [[0 for _ in range(self.num_of_vertex)] for _ in range(self.num_of_vertex)]
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                if i != j and matrix[i][j] == 0:
                    weight = randint(self.low_limit, self.upper_limit)
                    matrix[i][j] = weight
                    matrix[j][i] = weight
        return matrix
        # return [[0 if col == row else randint(self.low_limit, self.upper_limit) for col in range(self.num_of_vertex)] for row in range(self.num_of_vertex)]

