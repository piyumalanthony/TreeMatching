from Bio import Phylo
from ete3 import Tree

# iqtree_file = './examples/output.treefile'
# mcmctree_file = './examples/tree.nwk'

iqtree_file = '/home/piyumal/PHD/Hessian_experiments_v4/JC/iqtree_output/20/6000/output.treefile'
mcmctree_file = '/home/piyumal/PHD/Hessian_experiments_v4/JC/iqtree_output/20/6000/tree.nwk'


with open(iqtree_file, 'r') as f:
    iqtree_str = f.readline().strip()

with open(mcmctree_file, 'r') as f:
    mcmctree_str = f.readline().strip()

print("Iqtree string: ", iqtree_str)
print("Mcmctree String: ", mcmctree_str)

# tree = Phylo.read(iqtree_file, "newick")
# print(tree)
# tree.clade.name = "abc"
# print(tree)

tree_v2 = Tree(iqtree_file)
tree_v2.name = "root_v1"
tree_v2.get_common_ancestor("T1", "T2").name = "T1:T2"
print(tree_v2)

iqtree_nodes_traversal = []
for node in tree_v2.traverse("preorder"):
    # print("node: ", node)
    # print(node.get_edges())
    print("_____________________________")
    edge = node.get_edges()[0]
    clade_1 = list(edge[0])
    clade_2 = list(edge[1])
    node_name = clade_1 + clade_2
    node_name = [node.name for node in node_name]
    node_name.sort()
    node_name = ':'.join(node_name)
    node.name = node_name
    print(node)
    print(node.name)
    iqtree_nodes_traversal.append(node.name)

tree_v3 = Tree(mcmctree_file)

mcmctree_node_traversal = []
for node in tree_v3.traverse("preorder"):
    # print("node: ", node)
    # print(node.get_edges())
    print("_____________________________")
    edge = node.get_edges()[0]
    clade_1 = list(edge[0])
    clade_2 = list(edge[1])
    node_name = clade_1 + clade_2
    node_name = [node.name for node in node_name]
    node_name.sort()
    node_name = ':'.join(node_name)
    node.name = node_name
    print(node)
    print(node.name)
    mcmctree_node_traversal.append(node.name)


print(tree_v2)

print("############################")
mcmctreeroot = ''
iqtreeroot = ''
for i in mcmctree_node_traversal:
    if i not in iqtree_nodes_traversal:
        iqtreeroot = i

for j in iqtree_nodes_traversal:
    if j not in mcmctree_node_traversal:
        mcmctreeroot = j

iqtree_diff = list(set(mcmctree_node_traversal) - set(iqtree_nodes_traversal))
mcmctree_diff = list(set(iqtree_nodes_traversal) - set(mcmctree_node_traversal))

for iter, item in enumerate(iqtree_diff):
    index_diff = mcmctree_node_traversal.index(item)
    mcmctree_node_traversal[index_diff] = mcmctree_diff[iter]



# tree_v2.name = iqtreeroot
# tree_v3.name = mcmctreeroot
# mcmctree_node_traversal[0] = mcmctreeroot
# iqtree_nodes_traversal[0] = iqtreeroot
mcmctree_idx = [i for i in range(2*len(tree_v2.get_leaves())-3)]
iqtree_idx = []

# index_iqtree_diff = mcmctree_node_traversal.index(iqtreeroot)
# mcmctree_node_traversal[index_iqtree_diff] = mcmctreeroot
mcmctree_node_traversal = mcmctree_node_traversal[1:]


for val in iqtree_nodes_traversal[1:]:
    iqtree_idx.append(mcmctree_node_traversal.index(val))

# root = False
# for index, node in enumerate(tree_v2.traverse("preorder")):
#     node_name = node.name
#     if node.name == mcmctree_idx:
#         root = True
#     idx = mcmctree_node_traversal.index(node_name)
#     if root:
#      iqtree_idx.append(idx-1)
#     else:
#         iqtree_idx.append(idx)


print(iqtree_idx)




# def assign_internal_names(tree_):
#     if tree_.name == '':
#         child_0 = tree_.children[0]
#         child_1 = tree_.children[1]
#         child_2 = tree_.children[2]
#         if child_0.is_leaf():
#             if child_1.is_leaf():
#                 temp_name = [child_0.name, child_1.name]
#                 temp_name.sort()
#                 temp_name = ":".join(temp_name)
#                 tree_.name = temp_name
#                 return tree_
#             elif child_1.name != '':
#                 temp_name = [child_0.name] + list(child_1.name.split(":"))
#                 temp_name.sort()
#                 temp_name = ":".join(temp_name)
#                 tree_.name = temp_name
#                 return tree_
#             elif child_2.is_leaf():
#                 temp_name = [child_0.name, child_2.name]
#                 temp_name.sort()
#                 temp_name = ":".join(temp_name)
#                 tree_.name = temp_name
#                 return tree_
#             elif child_2.name != '':
#                 temp_name = [child_0.name] + list(child_2.name.split(":"))
#                 temp_name.sort()
#                 temp_name = ":".join(temp_name)
#                 tree_.name = temp_name
#                 return tree_
#             else:
#                 return assign_internal_names(child_1)
