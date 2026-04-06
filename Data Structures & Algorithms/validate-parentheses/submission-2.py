class Solution:
    def isValid(self, s: str) -> bool:
        if ((len(s))%2) != 0:
            return False
        valid = {"{":"}", "[":"]", "(":")"}
        stack = []
        for i in range(len(s)):
            if s[i] in valid:  # Opening bracket
                stack.append(s[i])
            elif stack and s[i] == valid[stack[-1]]:  # Closing bracket matches the top of the stack
                stack.pop()
            else:  # Invalid closing bracket or unmatched
                return False
    
        return not stack

        

        # num = len(s)-1;

        # for i in range(len(s)//2):
        #     if s[i] not in hashmap:
        #         hashmap[i] = s[i]
        #         checkval = valid.get(hashmap[i]) 
        #         if s[num] != checkval:
        #             return False
        #         else:
        #             num = num - 1
        #             continue
        
        # return True
   
       
