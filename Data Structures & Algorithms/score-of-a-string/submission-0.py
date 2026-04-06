class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0 

        for i in range(len(s) - 1):
            
            sum += abs(ord(s[i]) - ord(s[i + 1]))
            print(ord(s[i]))
            print(ord(s[i + 1]))
            sum = abs(sum)

        return sum
        c-o
        o-d
        d-e