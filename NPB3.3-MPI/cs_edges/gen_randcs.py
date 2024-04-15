import networkx as nx
import random
import argparse
import numpy as np

def generate_random_perfect_matching(graph, seed):
    rs = np.random.RandomState(seed)
    nodes = list(graph.nodes())
    rs.shuffle(nodes)
    matching_edges = [(nodes[i], nodes[i + 1]) for i in range(0, len(nodes), 2)]
    matching_graph = nx.Graph()
    matching_graph.add_edges_from(matching_edges)
    return matching_graph

def generate_random_IO_matching(gragh, seed):
    rs_1 = np.random.RandomState(seed)
    rs_2 = np.random.RandomState(seed + 1000)
    nodes_1 = list(gragh.nodes)
    nodes_2 = list(gragh.nodes)
    rs_1.shuffle(nodes_1)
    rs_2.shuffle(nodes_2)
    flag = False
    while flag:
        for i in range(0, len(nodes_1)):
            if (nodes_1[i] == nodes_2[i]):
                if (i+1 == len(node_1))
                    swap = nodes_2[i] 
                    nodes_2[i] = nodes_2[0]
                    nodes_2[0] = swap
                    i=0
                    break
                else:
                    swap = nodes_2[i]
                    nodes_2[i] = nodes_2[i+1]
                    nodes_2[i+1] = swap
                    i=0
                    break
            flag = True
    
    matching_edges = [(nodes_1[i], nodes_2[i]) for i in range(0, len(nodes_1))]
    matching_gragh = nx.Gragh()
    matching_gragh.add_edges_from(matching_edges)
    return matching_gragh

def gen_randcs(n_nodes, seed):
    complete_graph = nx.complete_graph(n_nodes)
    #random_matching = generate_random_perfect_matching(complete_graph, seed)
    random_matching = generate_random_IO_matching(complete_graph, seed)
    
    return random_matching

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='get node size')
    parser.add_argument('node_size', type=int, help='node size')
    parser.add_argument('seed', type=int, help='random seed')
    args = parser.parse_args()
    node_size = args.node_size
    seed = args.seed
    
    G_randcs = gen_randcs(node_size, seed)
    print(G_randcs.edges)
    #nx.write_edgelist(G_randcs, "randcs_{}_{}.edges".format(node_size, seed), data=False)
    nx.write_edgelist(G_randcs, "randcs_IO_{}_{}.edges".format(node_size, seed), data=False)
