class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell:
                    top = mat[i-1][j] if i else float('inf')
                    left = mat[i][j-1] if j else float('inf')
                    mat[i][j] = min(top, left) + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if cell := mat[i][j]:
                    bottom = mat[i+1][j] if i < m - 1 else float('inf')
                    right = mat[i][j+1] if j < n - 1 else float('inf')
                    mat[i][j] = min(cell, bottom + 1, right + 1)
        return mat
    
    
    
    def brute_force_updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.mat = mat
        self.m = len(mat)-1
        self.n = len(mat[0])-1
        result = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                result[i][j] = self.helper(i, j, 0)
                
               
        return result
                
        
        
        
        
    def helper(self, a, b, dist):
        if (a < 0) or  (a > self.m) or (b < 0) or (b > self.n):
            return float('inf')
        if self.mat[a][b] == -1:
            return float('inf')
        
        if self.mat[a][b] == 0:
            return dist
        self.mat[a][b] = -1
        dist = dist + 1
        
        left = self.helper(a, b-1, dist)
        right = self.helper(a, b+1, dist)
        up = self.helper(a-1, b, dist)
        down = self.helper(a+1, b, dist)
        self.mat[a][b] = 1
        return min(left, right, up, down)
            
            
        