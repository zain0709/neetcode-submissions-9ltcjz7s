class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []
        pacific = [[False] * COLS for _ in range(ROWS)]
        atlantic = [[False] * COLS for _ in range(ROWS)]
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def bfs(source, ocean):
            queue = deque(source)
            for r, c in source:
                ocean[r][c] = True
            while queue:
                r,c = queue.popleft()

                

                for dr, dc in directions:
                    nr, nc = r + dr, c  + dc

                    if nr in range(ROWS) and nc in range(COLS) and heights[nr][nc] >= heights[r][c] and not ocean[nr][nc]:
                        queue.append((nr,nc))
                        ocean[nr][nc] = True
                
        
        pac = []
        atl = []

        for r in range(ROWS):
            pac.append((r, 0))
            atl.append((r, COLS -1))

        for c in range(COLS):
            pac.append((0, c))
            atl.append((ROWS -1, c))

        bfs(pac, pacific)
        bfs(atl, atlantic)


        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    res.append((r,c))
        
        return res