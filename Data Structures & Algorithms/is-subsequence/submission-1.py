class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1, t1 = 0, 0

        while t1 < len(t) and s1 < len(s):
            if t[t1] == s[s1]:
                t1 += 1
                s1 += 1
            else:
                t1 += 1

        return len(s) == s1