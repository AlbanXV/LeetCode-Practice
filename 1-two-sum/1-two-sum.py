class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = dict()
        
        for i, el in enumerate(nums):
            comp = target - el
            
            if comp in values:
                return [values[comp], i]
            
            values[el] = i
        
        return []