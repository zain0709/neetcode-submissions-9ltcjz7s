class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:                            
        hashMap = defaultdict(list)
        visiting = set()             

        for course, pre in prerequisites:
            hashMap[course].append(pre)
            
        def dfs(course):
            

            if course in visiting:
                return False

            if hashMap[course] == []:
                return True

            visiting.add(course)

            for pre in hashMap[course]:
                 if not dfs(pre):
                    return False

            visiting.remove(course)
            hashMap[course] = []
            return True
                   


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True                


        