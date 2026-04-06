class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l  = 0
        r = len(s) -1

        while l < r:

            if s[l].isalnum() != True or s[l] == " ":
                l+=1
                continue 
            if s[r].isalnum() != True or s[r] == " ":
                r-=1
                continue 
            if s[l] != s[r]:
                return False
            
            r-=1
            l+=1

        return True

