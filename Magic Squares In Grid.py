class Solution:

    def distinct_checker(self, grid, row, col):
        nums = set()
        for i in range(3):
            for j in range(3):
                if grid[row+i][col+j] in nums or grid[row+i][col+j]>9 or grid[row+i][col+j]<=0:
                    return False
                nums.add(grid[row+i][col+j])
        return len(nums)==9

    def col_sum_finder(self, grid, row, col):
        col_res = 0
        for i in range(3):
            col_res += grid[row+i][col]
        return col_res

    def diagonal_sum_finder(self, grid, row, col):
        d1, d2 = 0, 0
        for i in range(3):
            d1 += grid[row+i][col+i]
            d2 += grid[row+i][col+2-i]
        return d1 == d2

    def solve(self, grid, row, col):
        if not self.distinct_checker(grid, row, col): return False

        row_sum = sum(grid[row][col:col+3])
        if sum(grid[row+1][col:col+3])!=row_sum or sum(grid[row+2][col:col+3])!=row_sum:
            return False
        
        col_sum = self.col_sum_finder(grid, row, col)
        if self.col_sum_finder(grid, row, col+1)!=col_sum or self.col_sum_finder(grid, row, col+2)!=col_sum:
            return False

        return self.diagonal_sum_finder(grid, row, col)
        

    def numMagicSquaresInside(self, grid) -> int:
        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.solve(grid, i, j):
                    res += 1
        return res
    
sol = Solution()
grid = [[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]]
print(sol.numMagicSquaresInside(grid))