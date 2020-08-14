class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()
        for count, num in enumerate(nums):
            if target - num in nums_map:
                return nums_map[target-num], count
            nums_map[num] = count
