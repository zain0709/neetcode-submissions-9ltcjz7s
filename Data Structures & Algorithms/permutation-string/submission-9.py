class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = 0
        res = ""
        newS = list(s1)

        if len(s1) > len(s2):
            return False

        for r in range(len(s2)):
            if s2[r] in s1 and r+len(s1) <= len(s2):
                print(s2[r])
                res += (s2[r:r+len(s1)])
                # print(res)
                sortedS = sorted(s1)
                res = sorted(res)

                if res == sortedS:
                    return True

                else:
                    print(res)
                    res = ""
                    print(res)

        return False