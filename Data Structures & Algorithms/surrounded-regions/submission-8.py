class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or i == ROWS-1 or j==0 or j==COLS-1:
                    if board[i][j] == 'O':
                        board[i][j] = 'T'
                        queue.append((i, j))
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
        
                    
