# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        counter = 0
        q = deque()
        node=( root, counter)
        q.append(node)
        hashMap = defaultdict(list)
        output = []

        while q:

            value, counter = q.popleft()

            left = value.left
            right = value.right

            if left:
                q.append((left, counter +1))

            if right:
                q.append((right, counter +1))

            hashMap[counter].append(value.val)

        for x,y in hashMap.items():
            output.append(y[-1])
        
        return output
