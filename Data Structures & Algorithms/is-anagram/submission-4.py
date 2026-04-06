class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
       
        y = sorted(s)
        z = sorted(t)
        return y == z