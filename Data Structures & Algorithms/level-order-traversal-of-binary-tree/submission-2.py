# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output= []
        hashMap = defaultdict(list)
        counter = 0
        node = (root,counter)
        q = deque()
        q.append(node)
        
        while q:
            valPopped, counter = q.popleft()
            left = valPopped.left
            right = valPopped.right
            if left:
                q.append((left, counter+1))
            if right:
                q.append((right, counter+1))

            hashMap[counter].append(valPopped.val)
        
        for x, y in hashMap.items():
            output.append(y)
        return output
        