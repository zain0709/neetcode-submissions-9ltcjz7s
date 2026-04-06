class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r = 0, len(s)-1
        newStack = []
        value, value2 = False, False
        def isPalindrome(l, r):
            while l <= r: 
                if s[l] != s[r]:
                   return False
                else:
                    l += 1
                    r -= 1
            return True

        while l <= r: 
            if s[l] != s[r]:
                return isPalindrome(l+1, r) or isPalindrome(l, r-1)
                break
            else:
                l += 1
                r -= 1

        return True 