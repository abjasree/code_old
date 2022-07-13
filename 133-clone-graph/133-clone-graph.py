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
        d = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()
                for neigh in curr_node.neighbors:
                    if neigh not in d:
                        d[neigh] = Node(neigh.val)
                        queue.append(neigh)
                    d[curr_node].neighbors.append(d[neigh])
                    
        return d[node]