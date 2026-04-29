class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        lists = list(count.values())
        print(lists)
        items = list(count.keys())
        print(items)
        for y in range(len(lists)):
            if lists[y] >= (len(nums) // 2):
                return items[y]
