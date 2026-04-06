class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')

        for i in range(len(nums)):
            total = 0
            count = 0
            while i <= r and r < len(nums):

                total += nums[r]
                count +=  1
                if total >= target:
                    print(r)
                    res = min(res, count)
                    r = i + 1
                    break
                
                elif r == len(nums) and total < target:
                    return 0 if type(res) != int else res

                r += 1


        return 0 if type(res) != int else res

        


            
