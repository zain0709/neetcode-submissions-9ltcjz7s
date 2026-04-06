class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            check_val = target - nums[i]
            if check_val in nums and nums.index(check_val) != i:
                output.append(nums.index(check_val))
                output.append(i)
                output = sorted(output)
                return output
        return []