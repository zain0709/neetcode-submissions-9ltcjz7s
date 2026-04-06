class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        queue  = deque()
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        time = 0

        while queue or max_heap:
            time += 1

            if max_heap:
                val = heapq.heappop(max_heap) + 1

                if val != 0:
                    queue.append( (val, (n+time)) )

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time




        
        


        




