class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize prefix and postfix arrays
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output = [1] * len(nums)
        
        # Build prefix product array
        prefix[0] = 1  # No prefix for the first element
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        # Build postfix product array
        postfix[-1] = 1  # No postfix for the last element
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        
        # Combine prefix and postfix for output
        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]
        
        return output