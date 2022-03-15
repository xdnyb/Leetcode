class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])    
        DIR = [0, 1, 0, -1, 0]
        q = deque([])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1
        
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == rows or nc < 0 or nc == cols or mat[nr][nc] != -1 : continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat
        
        
