class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()
        for index, num in enumerate(nums):
            nums_map[num] = index
        for index, num in enumerate(nums):
            if target - num in nums_map and index != nums_map[target-num]:
                return nums.index(num), nums_map[target-num]
