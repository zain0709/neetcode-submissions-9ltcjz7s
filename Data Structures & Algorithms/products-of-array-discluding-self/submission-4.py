class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
    
        prefixSum = [0] * n

        prefixSum[0] = nums[0]

        output = [1] * len(nums)
        pre = 1
        for i in range(n):
            prefixSum[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):

            output[i] = post * prefixSum[i]
            post *=  nums[i]

        return output



        
        
        return prefixSum

