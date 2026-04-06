class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i, task in enumerate(tasks):
            tasks[i].append(i)
        
        tasks  = sorted(tasks)

        timer = 1
        heap = []
        res = []
        while tasks or heap:

            while tasks and timer >= tasks[0][0]:
                task = tasks.pop(0)
                heapq.heappush(heap, (task[1], task))
                
            if heap:
                value, processingTask = heapq.heappop(heap)
                timer += processingTask[1]
                res.append(processingTask[2])
            else:
                timer += 1
        return res