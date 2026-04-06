# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def bfs(p,q,root):
        
            if p.val > root.val and q.val > root.val: # right subtree
                return bfs(p,q,root.right)

            if p.val == root.val or q.val == root.val: 
                return root

            if p.val < root.val and q.val < root.val: # left subtree
                return bfs(p,q,root.left)

            if p.val < root.val and q.val > root.val or  p.val > root.val and q.val < root.val:
                return root

        return bfs(p,q,root)