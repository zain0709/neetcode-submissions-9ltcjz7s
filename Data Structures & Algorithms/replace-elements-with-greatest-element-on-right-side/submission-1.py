class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newarr = [0] * len(arr)
        for i in range(len(arr)-1):
            newarr[i] = max(arr[i+1:])
        
        newarr[-1] = -1
        return newarr  