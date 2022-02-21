class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if r and c:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
                elif r:
                    grid[r][c] += grid[r - 1][c]
                elif c:
                    grid[r][c] += grid[r][c - 1]
        
        return grid[-1][-1]