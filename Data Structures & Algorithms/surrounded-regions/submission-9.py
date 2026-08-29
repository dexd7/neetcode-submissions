class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS-1 or c == COLS-1 )and board[r][c] == 'O':
                    board[r][c] = 'T'
                    queue.append((r, c))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                newr, newc = r+dr, c+dc
                if 0<=newr<ROWS and 0<=newc<COLS and board[newr][newc] == 'O':
                    board[newr][newc] = 'T'
                    queue.append((newr, newc))
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        

