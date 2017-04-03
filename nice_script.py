#!/usr/bin python3
# import sys
import networkx as nx


class GraphFileReader(object):
    def __init__(self, file_name):
        self.file_name = file_name
        # self.edge_set = {}
        self.vertex_type_dic = {}
        # self.graph = Graph(2)
