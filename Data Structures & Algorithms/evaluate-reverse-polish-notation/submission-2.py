class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            
            if i != "+" and i != "-"  and i != "*"  and i != "/":
                stack.append(int(i))
            
            if i == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                
                stack.append(val1 + val2)
            if i == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            if i == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 * val2)
            if i == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))  
        output = stack.pop()
        return output