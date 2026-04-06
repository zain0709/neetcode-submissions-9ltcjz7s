class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{",")": "(", "]": "["}
        my_stack = []
        for i in s:
            if  i in closeToOpen:
                if my_stack and my_stack[-1] == closeToOpen[i]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(i)
        return True if not my_stack else False