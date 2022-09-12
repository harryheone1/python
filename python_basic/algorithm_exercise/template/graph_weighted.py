# Solution1: https://blog.csdn.net/DXY587542/article/details/111822927
# two classes Vertex and Graph
# Vertex
# id
# edge: connect_to: id -> weight
# connect: connect self vertex to another node
# other: to_string, get_id, get_weight

# Graph
# vertex_list: all vertex of the Graph
# optional: num_of_ver
# add_vertex
# add_edge
# other: iter, contains


"""
Solution2:
Specific for leetcode 399
Graph: dict = id -> connect_to
connect_to:
1) dict = id -> weight
2) list = tuple(id, weight)
so,
a   -> b    -> e
    -> c
    -> d
"""


