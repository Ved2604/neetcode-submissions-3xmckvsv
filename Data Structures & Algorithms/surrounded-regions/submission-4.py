class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        seen = set()

        def collect(r, c):
            stack = [(r, c)]
            cells = []
            escapes = False
            while stack:
                row, col = stack.pop()
                if (row, col) in seen:
                    continue
                seen.add((row, col))
                cells.append((row, col))
                if row in (0, m-1) or col in (0, n-1):
                    escapes = True
                for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O" and (nr,nc) not in seen:
                        stack.append((nr, nc))
            return cells, escapes

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r, c) not in seen:
                    cells, escapes = collect(r, c)
                    if not escapes:
                        for row, col in cells:
                            board[row][col] = "X"