class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for string in strs:
            letter = [0] * 26
            for c in string:
                letter[ord(c) - ord('c')] += 1
            count[tuple(letter)].append(string)
        print(count)
        
        return list(count.values())
        
     




































# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:

#             count = [0] * 26
#             for c in s:
                
#                 count[ord(c) - ord('a')] += 1

#             res[tuple(count)].append(s)

#         return list(res.values())















