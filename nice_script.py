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
    def construct_graph_from_file(self, file_name):
        f = open(file_name)
        self.vertex_type_dic = {}
        try:
            for line in f:
                if "<edge source=" in line:
                    break
                if "<node id=" in line:
                    if "type" not in line:
                        raise Exception("Error! Found vertex without a type. Exit")
                    line = line[10:]
                    stop = line.index('"')
                    v_id = int(line[0:stop])
                    line = line[stop+8:]
                    stop = line.index('"')
                    v_type = line[0:stop]
                    if v_id in self.vertex_type_dic:
                        raise Exception("Error! Possible duplicate vertex. Exit")
                    self.vertex_type_dic[v_id] = v_type

            f.close()
            assert len(self.vertex_type_dic) > 1
        except Exception as er:
            print(er)
            return

        print("Successfully constructed vertex set")
        print(self.vertex_type_dic)
