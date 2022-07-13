"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        dict_nodes = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()
                for neigh in curr_node.neighbors:
                    if neigh not in dict_nodes:
                        dict_nodes[neigh] = Node(neigh.val)
                        queue.append(neigh)
                    dict_nodes[curr_node].neighbors.append(dict_nodes[neigh])
                    
        return dict_nodes[node]