class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sets = set(nums)
        test = {}
        output = []
        print(sets)
        for s in sets:
            test[s] = nums.count(s)
        for i in range(k):
            max_key = max(test, key=test.get)
            del test[max_key]
            output.append(max_key)
        return output