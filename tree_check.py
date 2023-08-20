# import numpy as np
#
# iqtree_nodes_traversal_1 = ['T1:T10:T11:T12:T13:T14:T15:T16:T17:T18:T19:T2:T20:T3:T4:T5:T6:T7:T8:T9', 'T11', 'T10', 'T1:T12:T13:T14:T15:T16:T17:T18:T19:T2:T20:T3:T4:T5:T6:T7:T8:T9', 'T1:T2:T3:T4:T5:T6:T7:T8:T9', 'T9', 'T1:T2:T3:T4:T5:T6:T7:T8', 'T8', 'T1:T2:T3:T4:T5:T6:T7', 'T7', 'T1:T2:T3:T4:T5:T6', 'T6', 'T1:T2:T3:T4:T5', 'T5', 'T1:T2:T3:T4', 'T4', 'T1:T2:T3', 'T3', 'T1:T2', 'T2', 'T1', 'T12:T13:T14:T15:T16:T17:T18:T19:T20', 'T17:T18:T19:T20', 'T19:T20', 'T20', 'T19', 'T17:T18', 'T18', 'T17', 'T12:T13:T14:T15:T16', 'T15:T16', 'T16', 'T15', 'T12:T13:T14', 'T14', 'T12:T13', 'T13', 'T12']
# mcmctree_node_traversal_1 = ['T1:T10:T11:T12:T13:T14:T15:T16:T17:T18:T19:T2:T20:T3:T4:T5:T6:T7:T8:T9', 'T1:T10:T11:T2:T3:T4:T5:T6:T7:T8:T9', 'T10:T11', 'T11', 'T10', 'T1:T2:T3:T4:T5:T6:T7:T8:T9', 'T9', 'T1:T2:T3:T4:T5:T6:T7:T8', 'T8', 'T1:T2:T3:T4:T5:T6:T7', 'T7', 'T1:T2:T3:T4:T5:T6', 'T6', 'T1:T2:T3:T4:T5', 'T5', 'T1:T2:T3:T4', 'T4', 'T1:T2:T3', 'T3', 'T1:T2', 'T2', 'T1', 'T17:T18:T19:T20', 'T19:T20', 'T20', 'T19', 'T17:T18', 'T18', 'T17', 'T12:T13:T14:T15:T16', 'T15:T16', 'T16', 'T15', 'T12:T13:T14', 'T14', 'T12:T13', 'T13', 'T12']
#
# iqtree_nodes_traversal_2 = ['T1:T10:T11:T12:T13:T14:T15:T16:T17:T18:T19:T2:T20:T3:T4:T5:T6:T7:T8:T9', 'T11', 'T10', 'T1:T12:T13:T14:T15:T16:T17:T18:T19:T2:T20:T3:T4:T5:T6:T7:T8:T9', 'T1:T2:T3:T4:T5:T6:T7:T8:T9', 'T9', 'T1:T2:T3:T4:T5:T6:T7:T8', 'T8', 'T1:T2:T3:T4:T5:T6:T7', 'T7', 'T1:T2:T3:T4:T5:T6', 'T6', 'T1:T2:T3:T4:T5', 'T5', 'T1:T2:T3:T4', 'T4', 'T1:T2:T3', 'T3', 'T1:T2', 'T2', 'T1', 'T12:T13:T14:T15:T16:T17:T18:T19:T20', 'T17:T18:T19:T20', 'T19:T20', 'T20', 'T19', 'T17:T18', 'T18', 'T17', 'T12:T13:T14:T15:T16', 'T15:T16', 'T16', 'T15', 'T12:T13:T14', 'T14', 'T12:T13', 'T13', 'T12']
# mcmctree_node_traversal_2 = ['T1:T10:T11:T12:T13:T14:T15:T16:T17:T18:T19:T2:T20:T3:T4:T5:T6:T7:T8:T9', 'T1:T10:T11:T2:T3:T4:T5:T6:T7:T8:T9', 'T10:T11', 'T11', 'T10', 'T1:T2:T3:T4:T5:T6:T7:T8:T9', 'T9', 'T1:T2:T3:T4:T5:T6:T7:T8', 'T8', 'T1:T2:T3:T4:T5:T6:T7', 'T7', 'T1:T2:T3:T4:T5:T6', 'T6', 'T1:T2:T3:T4:T5', 'T5', 'T1:T2:T3:T4', 'T4', 'T1:T2:T3', 'T3', 'T1:T2', 'T2', 'T1', 'T17:T18:T19:T20', 'T19:T20', 'T20', 'T19', 'T17:T18', 'T18', 'T17', 'T12:T13:T14:T15:T16', 'T15:T16', 'T16', 'T15', 'T12:T13:T14', 'T14', 'T12:T13', 'T13', 'T12']
#
#
# print(set(iqtree_nodes_traversal_1) - set(mcmctree_node_traversal_1))
# print("--------------------------------------------------------------")
# print(set(iqtree_nodes_traversal_2) - set(mcmctree_node_traversal_2))
#
#
# for i in iqtree_nodes_traversal_2:
#     if i not in mcmctree_node_traversal_1:
#         print(i)

# a = ['a', 'b', 'c', 'd', 'f']
# for i,j in enumerate(a):
#     print(j)
#     a = a[i:]
#     print(a)
array = [1, 1, 1, 1, 1]
sequence = [1, 1, 1]


def isValidSubsequence(array, sequence):
    if len(sequence) == 0:
        return True
    elif len(sequence) > 0 and len(array) == 0:
        return False
    elif len(sequence) > len(array):
        return False
    sequence_item = sequence[0]
    index = 0
    match_flag = False
    for i, item in enumerate(array):
        if item == sequence_item:
            index = i
            match_flag = True
    if match_flag:
        return isValidSubsequence(array[index + 1:], sequence[1:])
    else:
        return False

print(isValidSubsequence(array,sequence))