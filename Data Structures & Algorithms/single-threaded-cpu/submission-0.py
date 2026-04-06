class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index, task in enumerate(tasks):
            task.append(index)

        res = []
        tasks = sorted(tasks)
        
        timer = 0
        heap = []

        while tasks or heap:
            # add all available tasks
            while tasks and timer >= tasks[0][0]:
                task = tasks.pop(0)
                heapq.heappush(heap, (task[1], task))  # FIX: push as tuple

            if heap:
                priority, processingTask = heapq.heappop(heap)
                print(priority, processingTask)
                timer += processingTask[1]
                res.append(processingTask[2])
            else:
                timer += 1  # idle

        return res