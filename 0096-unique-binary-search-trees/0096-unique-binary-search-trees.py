class Solution:
    def numTrees(self, n: int) -> int:
        
        # Time: O(n^2)
        
        x = [0] * (n + 1)
        
        x[0] = 1
        x[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                
                x[i] += x[j - 1] * x[i - j]
        
        return x[n]
        
        '''
        if n <= 1:
            return 1
        
        return sum(self.numTrees(i - 1) * self.numTrees(n - i) for i in range (1, n + 1))
        '''