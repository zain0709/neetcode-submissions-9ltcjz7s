class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        newStack = []
        operationStack = ["+" , "C" , "D"]
        for operation in operations:
            if operation not in operationStack:
                newStack.append(int(operation))
            elif operation == "+":
                value1 = newStack[-1]
                value2 = newStack[-2]
                newStack.append(value1 + value2)
            elif operation == "C":
                newStack.pop()
            elif operation == "D":
                value1 = newStack[-1]
                newStack.append(value1 * 2)
        return sum(newStack)
