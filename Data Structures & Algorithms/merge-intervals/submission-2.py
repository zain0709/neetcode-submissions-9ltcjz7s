class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # maps = {}
        # my_list = []
        # for i in range(len(intervals)):
        #     for j in range(1):
        #         if intervals[i][j] not in maps:
        #             maps[intervals[i][j]] = intervals[i][j+1]
                    
        #         if intervals[i][j] in maps:
        #             if intervals[i][j+1] > maps[intervals[i][j]]:
        #                 maps[intervals[i][j]] = intervals[i][j+1]
        #         if intervals[i][j+1] in maps[intervals[i][j]]:
        #             if 
        # for v,k in maps.items():
        #     my_list.append([v,k])
        # return my_list

        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] 
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output 