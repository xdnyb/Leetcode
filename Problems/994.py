class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [0 , 1, 0, -1, 0]
        m, n = len(grid), len(grid[0])
        q = deque([])
        times = 0
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        temp = deque([])
        if not q:
            if fresh == 0: return 0
        while q:
            print(q)
            r,c = q.popleft()
            
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i+1]
                if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] != 1: continue
                grid [nr][nc] += 1
                fresh -= 1
                print("fresh", fresh)
                temp.append((nr, nc))
                print("to be:", temp)
            if not q:
                times += 1
                print("times:", times)
                while temp:
                    q.append(temp.popleft())
            print("after temp:", q)
            
        if fresh == 0 : return times - 1
        
        return -1
