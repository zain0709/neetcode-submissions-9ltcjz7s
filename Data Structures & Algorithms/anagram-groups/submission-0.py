from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs2 = [''] * len(strs)
        for i in range(len(strs)):
            strs2[i] = ''.join(sorted(strs[i]))
        output = []
        while strs2:
            current = strs2[0]
            listappend = []
            indices_to_remove = []
            for j in range(len(strs2)):
                if strs2[j] == current:
                    listappend.append(strs[j])
                    indices_to_remove.append(j)
            for index in sorted(indices_to_remove, reverse=True):
                strs2.pop(index)
                strs.pop(index)
            output.append(listappend)
        return output
