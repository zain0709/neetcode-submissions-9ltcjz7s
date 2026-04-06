"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashMap = {}
        def dfs(currNode):
            if currNode in hashMap:
                return hashMap[currNode]
            clone = Node(currNode.val) #making a new node with same val as the org 
            hashMap[currNode] = clone

            for neighbor in currNode.neighbors:
                clone_neighbour = dfs(neighbor)
                clone.neighbors.append(clone_neighbour)
            return clone

        return dfs(node)



