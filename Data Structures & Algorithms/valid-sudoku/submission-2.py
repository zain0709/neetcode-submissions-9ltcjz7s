class Solution:
    # def column(self, matrix, i):
    #     return [row[i] for row in matrix]
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for i in range(len(board)):
            
            
        #     count = len([x for x in board[i] if x.isdigit() and x != '.'])
        #     integer_set = {int(x) for x in board[i] if x.isdigit()}
        #     setVal = len(integer_set)
            
        #     col = self.column(board, i)
        #     countCol = len([x for x in col if x.isdigit() and x != '.'])
        #     integer_setCol = {int(x) for x in col if x.isdigit()}
        #     setValCol = len(integer_setCol)


        #     if count != setVal:
        #         return False 

        #     if countCol != setValCol:
        #         return False 
          
        # return True


    
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": 
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
            
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True