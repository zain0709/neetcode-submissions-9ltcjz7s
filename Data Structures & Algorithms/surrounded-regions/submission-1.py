class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]    
        borders = set()
        def dfs(borders):
            q = deque(borders)
         
                    
            while q:
                r,c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr in range(ROWS) and nc in range(COLS):
                            q.append((nr,nc))
                                  
        


        
        for r in range(ROWS):
            borders.add((r, 0))          # left column
            borders.add((r, COLS - 1))   # right column

        for c in range(COLS):
            borders.add((0, c))          # top row
            borders.add((ROWS - 1, c))   # bottom row

        dfs(borders)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
