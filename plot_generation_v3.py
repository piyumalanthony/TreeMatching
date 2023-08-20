import matplotlib.pyplot as plt
from ete3 import Tree
import numpy as np
import time
import random
import copy
from ordered_set import OrderedSet


random.seed(1)

for i in range(10, 110, 10):
    for j in range(1000, 11000, 1000):
        print("_______________________________________________________________________________________________________")
        print(i,j)
        iqtree_br = f'/home/piyumal/PHD/Hessian_experiments_v4/JC/iqtree_output/{i}/{j}/output_blengths.gh'
        mcmctree_br = f'/home/piyumal/PHD/Hessian_experiments_v4/JC/mcmctree_output/{i}/{j}/brLengths.txt'
        with open(iqtree_br) as f:
            data = f.readline()
            iqtree_blengths = data.strip().split()
            iqtree_blengths = [float(i) for i in iqtree_blengths]

        with open(mcmctree_br) as f:
            data = f.readline()
            mcmctree_blengths = data.strip().split()
            mcmctree_blengths = [float(i) for i in mcmctree_blengths]

        iqtree_file = f'/home/piyumal/PHD/Hessian_experiments_v4/JC/iqtree_output/{i}/{j}/output.treefile'
        mcmctree_file = f'/home/piyumal/PHD/Hessian_experiments_v4/JC/iqtree_output/{i}/{j}/tree.nwk'

        with open(iqtree_file, 'r') as f:
            iqtree_str = f.readline().strip()

        with open(mcmctree_file, 'r') as f:
            mcmctree_str = f.readline().strip()


        tree_v2 = Tree(iqtree_file)

        iqtree_nodes_traversal = []
        for node in tree_v2.traverse("preorder"):
            edge = node.get_edges()[0]
            clade_1 = list(edge[0])
            clade_2 = list(edge[1])
            node_name = clade_1 + clade_2
            node_name = [node.name for node in node_name]
            node_name.sort()
            node_name = ':'.join(node_name)
            node.name = node_name
            iqtree_nodes_traversal.append(node.name)

        tree_v3 = Tree(mcmctree_file)

        mcmctree_node_traversal = []
        for node in tree_v3.traverse("preorder"):
            edge = node.get_edges()[0]
            clade_1 = list(edge[0])
            clade_2 = list(edge[1])
            node_name = clade_1 + clade_2
            node_name = [node.name for node in node_name]
            node_name.sort()
            node_name = ':'.join(node_name)
            node.name = node_name
            mcmctree_node_traversal.append(node.name)

        # iqtree_diff = list(OrderedSet(mcmctree_node_traversal) - OrderedSet(iqtree_nodes_traversal))
        # # iqtree_diff = sorted(iqtree_diff, key=len)
        # mcmctree_diff = list(OrderedSet(iqtree_nodes_traversal) - OrderedSet(mcmctree_node_traversal))
        # mcmctree_diff = sorted(mcmctree_diff, key=len)

        iqtree_diff = []
        mcmctree_diff = []
        for u in mcmctree_node_traversal:
            if u not in iqtree_nodes_traversal:
                iqtree_diff.append(u)

        for v in iqtree_nodes_traversal:
            if v not in mcmctree_node_traversal:
                mcmctree_diff.append(v)
        iqtree_diff.reverse()
        mcmctree_node_traversal_1 = copy.deepcopy(mcmctree_node_traversal)
        for iter, item in enumerate(iqtree_diff):
            index_diff = mcmctree_node_traversal.index(item)
            mcmctree_node_traversal[index_diff] = mcmctree_diff[iter]

        mcmctree_idx = [i for i in range(2 * len(tree_v2.get_leaves()) - 3)]
        iqtree_idx = []

        mcmctree_node_traversal_post = mcmctree_node_traversal[1:]

        for val in iqtree_nodes_traversal[1:]:
            iqtree_idx.append(mcmctree_node_traversal_post.index(val))
        mcmc_blengths_v2 = []
        for l in iqtree_idx:
            mcmc_blengths_v2.append(mcmctree_blengths[l])

        print(iqtree_blengths)
        print(mcmc_blengths_v2)

        a = np.array(iqtree_blengths)
        b = np.array(mcmc_blengths_v2)

        z = a - b

        # time.sleep(3)
        print("iqtree brach length revised")
        plt.plot(a, b, 'bo',)
        plt.plot([min(a), max(a)], [min(a), max(a)], 'r--', label='x=y')
        plt.title(f'IQTree vs Baseml branch lengths for {i} taxa and {j} seq length')
        plt.xlabel('IQtree branch lengths')
        plt.ylabel('Baseml branch lengths')
        plt.savefig(f'/home/piyumal/PHD/Hessian_experiments_v4/JC/plots_v3/br_lengths_{i}_{j}.png')
        plt.clf()

        print("Delta:", z)
        print("IQTree traversal:", iqtree_nodes_traversal)
        print("MCMCTree traversal:",mcmctree_node_traversal_1)
        print("IQTree diff:", iqtree_diff)
        print("MCMCTree diff:", mcmctree_diff)
        print("_______________________________________________________________________________________________________")





