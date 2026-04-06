class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        sequence = 0

        for num in hash_set:
            if num - 1 not in hash_set:
                count = 0

                while num + count in hash_set:
                    count +=1
                
                sequence = max(count, sequence)

        return sequence
