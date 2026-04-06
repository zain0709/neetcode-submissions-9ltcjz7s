class TimeMap:

    def __init__(self):
        self.userMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.userMap:            
            self.userMap[key] = []
        self.userMap[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.userMap:
            return ""
        res = ""
        value = self.userMap[key]
        l,r = 0, len(value) - 1

        while l <= r: 

            mid = (l+r) // 2

            if value[mid][1] <= timestamp:
                res =  value[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res



