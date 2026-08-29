class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(COLS):
            if board[0][i] == 'O':
                queue.append((0, i))
                board[0][i] = 'T'
            if board[ROWS-1][i] == 'O':
                queue.append((ROWS-1, i))
                board[ROWS-1][i] = 'T'
        for i in range(1, ROWS-1):
            if board[i][0] == 'O':
                queue.append((i, 0))
                board[i][0] = 'T'
            if board[i][COLS-1] == 'O':
                queue.append((i, COLS-1))
                board[i][COLS-1] = 'T'

        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                newr, newc = r+dr, c+dc
                if 0<=newr<ROWS and 0<=newc<COLS and board[newr][newc] == 'O':
                    board[newr][newc] = 'T'
                    queue.append((newr, newc))
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        
                    
