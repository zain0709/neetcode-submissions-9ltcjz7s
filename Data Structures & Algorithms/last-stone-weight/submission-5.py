class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        sorted_stones = sorted(stones, reverse=True)
        stone1 = 0
        stone2 = 0
        for each in sorted_stones:
            heapq.heappush(max_heap, -each)

        while len(max_heap) >= 2:

            stone1 = abs(heapq.heappop(max_heap))
            stone2 = abs(heapq.heappop(max_heap))

            if stone1 < stone2 or stone1 > stone2:    
                num = abs(stone2 - stone1)
                if num != 0 or len(max_heap) == 0:
                    heapq.heappush(max_heap, -num)

        if max_heap:

            return abs(max_heap[0])
        else:
            return 0

