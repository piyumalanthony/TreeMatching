from ete3 import Tree

iqtree_file = '/home/piyumal/PHD/Hessian_experiments_v4/JC/iqtree_output/10/1000/output.treefile'
mcmctree_file = '/home/piyumal/PHD/Hessian_experiments_v4/JC/iqtree_output/10/1000/tree.nwk'


with open(iqtree_file, 'r') as f:
    iqtree_str = f.readline().strip()

with open(mcmctree_file, 'r') as f:
    mcmctree_str = f.readline().strip()

# print("Iqtree string: ", iqtree_str)
# print("Mcmctree String: ", mcmctree_str)


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


iqtree_diff = list(set(mcmctree_node_traversal) - set(iqtree_nodes_traversal))
mcmctree_diff = list(set(iqtree_nodes_traversal) - set(mcmctree_node_traversal))

for iter, item in enumerate(iqtree_diff):
    index_diff = mcmctree_node_traversal.index(item)
    mcmctree_node_traversal[index_diff] = mcmctree_diff[iter]

mcmctree_idx = [i for i in range(2*len(tree_v2.get_leaves())-3)]
iqtree_idx = []

mcmctree_node_traversal = mcmctree_node_traversal[1:]


for val in iqtree_nodes_traversal[1:]:
    iqtree_idx.append(mcmctree_node_traversal.index(val))

print(iqtree_idx)
