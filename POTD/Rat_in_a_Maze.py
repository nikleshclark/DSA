from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        def is_valid_move(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1 and (x, y) not in visited
        
        def dfs(x,y,path):
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return
            visited.add((x, y))
            
            for move, (dx, dy) in moves.items():
                nx, ny = x + dx, y + dy
                if is_valid_move(nx, ny):
                    dfs(nx, ny, path + move)
            
            visited.remove((x, y))
        if m[0][0] == 0:
            return []
        
        n = len(m)
        moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        paths = []
        visited = set()
        
        dfs(0, 0, "")
        
        return paths
    
print(Solution().findPath([[1, 0, 0, 0],[1, 1, 0, 1],[1, 1, 0, 0],[0, 1, 1, 1]]))


# Time Complexity: (O(4^{(n \times n)}))
# Space Complexity: (O(n^2)) for the visited set and the recursion stack in the worst case.