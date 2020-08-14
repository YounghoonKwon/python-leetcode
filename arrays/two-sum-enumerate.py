class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for count, num in enumerate(nums):
            complement = target - num
            if complement in nums[count+1:]:
                return count, nums[count+1:].index(complement) + (count+1)
                
                    
                    
