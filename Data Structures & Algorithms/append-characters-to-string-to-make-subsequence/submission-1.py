class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        s1, t1 = 0, 0

        while s1 < len(s) and t1 < len(t):
            if s[s1] == t[t1]:
                s1 += 1
                t1 += 1
            else:
                s1 += 1

        return len(t) - t1
