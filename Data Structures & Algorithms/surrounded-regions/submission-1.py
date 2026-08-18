class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        border_os = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i==0 or i==ROWS-1 or j==0 or j==COLS-1):
                    if board[i][j] == 'O':
                            board[i][j] = 'T'
                        
                            border_os.append((i,j))
                
                        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def bfs(starts):
            
            q = deque(starts)
            visited = set(starts)
            while q:
                r,c = q.popleft()
                for dx,dy in dirs:
                    nrow = r+dx
                    ncol = c+dy
                    if ( 0<=nrow<ROWS and
                         0<=ncol<COLS and
                         (nrow, ncol) not in visited and
                         board[nrow][ncol] == 'O'):
                         board[nrow][ncol] = 'T'
                         visited.add((nrow,ncol))
                         q.append((nrow,ncol))
        bfs(border_os)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        return
         


