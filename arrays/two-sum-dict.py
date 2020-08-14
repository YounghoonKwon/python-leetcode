class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()
        for count, num in enumerate(nums):
            nums_map[num] = count
        
        for count, num in enumerate(nums):
            if target - num in nums_map and count != nums_map[target-num]:
                return nums.index(num), nums_map[target-num]
