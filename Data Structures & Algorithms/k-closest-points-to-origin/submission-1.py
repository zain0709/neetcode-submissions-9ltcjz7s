class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [     ]
        res = []
        for x, y in points:
            distance = math.sqrt((0 - x)**2 + (0 - y)**2 )
            heapq.heappush(maxHeap, (distance, (x,y)))
            heapq.heapify(maxHeap)


        while k != 0:
            distance, points = heapq.heappop(maxHeap)
            res.append(points)
            k -= 1

                
        return res


        


