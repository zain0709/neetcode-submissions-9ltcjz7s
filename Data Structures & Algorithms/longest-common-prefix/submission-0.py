class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        myStr = strs[0]

        for word in range(1, len(strs)):
            while len(myStr) != 0 and myStr != strs[word][:len(myStr)]:
                    myStr = myStr[:-1]
            if len(myStr) > len(strs[word]):
                myStr = myStr[:len(strs[word])]

        return myStr