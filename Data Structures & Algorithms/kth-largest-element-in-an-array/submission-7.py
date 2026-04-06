class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        targetVal = len(nums) - k

        def quickSort(l, r):

            p = l
            pivot = nums[r]
            

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i] , nums[p]
                    p += 1
            nums[r], nums[p] = nums[p] , nums[r]

            if p < targetVal:
                return quickSort(p+1, r)
            
            elif p > targetVal:
                return quickSort(l, p-1)

            else:
                return nums[p]
        l = 0
        r = len(nums) -1
        return quickSort(l, r)

    
