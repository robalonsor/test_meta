#!/usr/bin python3
# import sys
import networkx as nx


class GraphFileReader(object):
    def __init__(self, file_name):
        self.file_name = file_name
        # self.edge_set = {}
        self.vertex_type_dic = {}
        # self.graph = Graph(2)
    def generate_graph(self):
            file_name = self.file_name
            try:
                f = open(file_name, 'r')
            except IOError:
                print('cannot open', file_name)
            else:
                print(file_name, 'has', len(f.readlines()), 'lines')
                print("Starting to parse Graphml file")
                f.close()
                self.construct_graph_from_file(file_name)
