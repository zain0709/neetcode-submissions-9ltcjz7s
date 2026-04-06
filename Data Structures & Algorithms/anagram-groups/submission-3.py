# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         lists = []

#         for i in range(len(strs)):
#             if strs[i] == '':
#                 continue
#             new_list = []
#             ogList = []
#             ogList.append(strs[i])
#             lists.append(ogList)
            
#             for j in range(i+1, len(strs)):
#                 if len(strs[i]) == len(strs[j]):
#                     if sorted(strs[i]) == sorted(strs[j]) and strs[i] != '':
#                         new_list.append(strs[j])
#                         strs[j] = ''
#                 if j == len(strs)-1:
#                     lists[i].extend(new_list)
#                     strs[i] = ''
#         print(lists)
#         return lists

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())