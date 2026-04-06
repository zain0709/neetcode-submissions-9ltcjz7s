class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newString = ""
        for i in range(len(word1)):
            newString += word1[i]
            if i < len(word2):
                newString += word2[i]
        if len(word1) < len(word2):
            newString += word2[len(word1):]
        return newString