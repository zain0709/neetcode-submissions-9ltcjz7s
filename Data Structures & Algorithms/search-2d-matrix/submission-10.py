class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r =  0, len(matrix) -1
        l2, r2 =  0, len(matrix[0]) -1
        index = 0
        for i in range(len(matrix)):
            if target < matrix[i][-1]:
                index = i
                break
            if target == matrix[i][-1]:
                return True
            
   

        while l2 <= r2:
            mid = (l2+r2) // 2
            if target == matrix[index][mid]:
                 return True
            elif target > matrix[index][mid]:
                l2 = mid +1
            elif target < matrix[index][mid]:
                r2 = mid - 1
        return False
            