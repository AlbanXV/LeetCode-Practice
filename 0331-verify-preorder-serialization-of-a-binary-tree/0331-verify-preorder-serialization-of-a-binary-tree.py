class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        nodes = preorder.split(',')
        
        c = 1
        
        for i in nodes:
            
            if c == 0:
                return False
            
            if i == '#':
                c -= 1
            else:
                c += 1
            
        return c == 0