class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ope = ["+" , "-", "*", "/"]
        myStack = []
        res = 0
        for i in range(len(tokens)):
            if tokens[i] in ope and myStack:
                val2 = myStack.pop()
                val1 = myStack.pop()
                if tokens[i] == "+":
                    res = int(val1) + int(val2)
                elif tokens[i] == "*":
                    res = int(val1) * int(val2)
                elif tokens[i] == "/":
                    res =int(val1)/int(val2)
                    

                elif tokens[i] == "-":
                    res = int(val1) - int(val2)

                myStack.append(res)
            else:
                myStack.append(tokens[i])
                print(myStack)

        return int(myStack[0])