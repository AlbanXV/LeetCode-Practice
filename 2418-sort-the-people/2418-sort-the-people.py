class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        # Selection Sort
        
        h = len(heights)
        
        for i in range(0, h-1):
            k = i
            height = heights[i]
            
            for j in range(i+1, h):
                if heights[j] > height:
                    height = heights[j]
                    k = j
            
            if i != k:
                heights[i], heights[k] = heights[k], heights[i]
                names[i], names[k] = names[k], names[i]
            
        return names
    