class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sets = set()

        sets.add("-")
        sets.add("+")
        sets.add("/")
        sets.add("*")
        myStack = []

        res = 0
        for i in range(len(tokens)):

            if tokens[i] in sets and myStack:
                val2 = myStack.pop()
                val1 = myStack.pop()
                if tokens[i] == "-":
                    res = int(val1) - int(val2)
                elif tokens[i] == "+":
                    res = int(val1) + int(val2)

                elif tokens[i] == "*":
                    res = int(val1) * int(val2)

                elif tokens[i] == "/":
                    res = int(val1) / int(val2)

                myStack.append(res)
            else:
                myStack.append(tokens[i])

        return int(myStack[0])
