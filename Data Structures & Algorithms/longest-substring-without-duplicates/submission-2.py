class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        maxCount = 0
        if len(s) == 0:
            return 0
        currentWindow = []

        for r in range(len(s)):
            while s[r] in currentWindow:
                l+=1
                currentWindow.pop(0)
                count -=1
            currentWindow.append(s[r])
            count +=1
            maxCount = max(count, maxCount)

        return maxCount