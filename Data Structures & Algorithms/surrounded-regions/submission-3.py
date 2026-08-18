class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        for i in range(ROWS):
            if board[i][0] == 'O':
                q.append((i,0))
                board[i][0] = 'T' 
            if board[i][COLS-1] == 'O':
                q.append((i, COLS-1))
                board[i][COLS-1] = 'T'
        for i in range(1,COLS-1):
            if board[0][i] == 'O':
                q.append((0,i))
                board[0][i] = 'T' 
            if board[ROWS-1][i] == 'O':
                q.append((ROWS-1, i))
                board[ROWS-1][i] = 'T'
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            r,c = q.popleft()
            for dx,dy in dirs:
                nr = r+dx
                nc = c+dy
                if (0<=nr<ROWS and
                    0<=nc<COLS and
                    board[nr][nc] == 'O'):
                    q.append((nr,nc))
                    board[nr][nc] = 'T'
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
        

