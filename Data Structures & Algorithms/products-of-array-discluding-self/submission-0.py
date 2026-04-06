class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        value = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    value *= nums[j] 
                else:
                    continue
            output[i] = value
            value = 1
        return output