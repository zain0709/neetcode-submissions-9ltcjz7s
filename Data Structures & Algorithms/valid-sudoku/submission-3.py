class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        column = set()
        box = set()


        for r in range(9):
            for c in range(9):
                
                sudoku = board[r][c]

                if sudoku == ".":
                    continue
            
                curr_row = (r, sudoku)
                curr_column = (c, sudoku)
                boxs = (r//3) * 3 + (c//3)
                curr_box = (boxs, sudoku)


                if curr_row in row or curr_column in column or curr_box in box:
                    return False

                row.add(curr_row)
                column.add(curr_column)
                box.add(curr_box)

        return True