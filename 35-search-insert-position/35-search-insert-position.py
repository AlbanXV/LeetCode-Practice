class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            i = (low + high) // 2
            
            if nums[i] == target:
                return i
            elif nums[i] < target:
                low = i + 1
            elif nums[i] > target:
                high = i - 1
        
        return low