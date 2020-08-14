class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        product = 1
        for index in range(0, len(nums)):
            product_list.append(product)
            product = product * nums[index]
            
        product = 1
        for index in range(len(nums) - 1, -1, -1):
            product_list[index] = product_list[index] * product
            product = product * nums[index]
            
        return product_list
            
            
            
        
        
        
