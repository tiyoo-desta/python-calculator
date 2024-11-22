def find_path(graph, current_node, end_node):
    if current_node == end_node:
        print(end_node)
        print ("")
    elif end_node.pred is None:
        print("impossible")
    else:
        find_path(graph, current_node, end_node.pred) # recursion
        print(end_node)
        print("othrer stuu")


class Node:
    def __init__(self, name):
        self.name = name
        self.pred = None  # predecessor node
    
    def __repr__(self):
        return self.name  # to print the node name when printing the path

# Create nodes
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")

# Set up predecessors to form a path: A -> B -> C -> D
node_b.pred = node_a
node_c.pred = node_b
node_d.pred = node_c

# Define the graph (not actually used in this function but included for completeness)
graph = [node_a, node_b, node_c, node_d]

# Example usage
find_path(graph, node_a, node_d)  # Should print A B C D
# find_path(graph, node_a, node_b)  # Should print A B
# find_path(graph, node_a, node_a)  # Should print A
# find_path(graph, node_a, Node("E"))  # Should print "impossible" because E has no predecessor
