class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # m is a table that holds the product of nums at idx [i, j)
        m = {(i, i+1): nums[i] for i in range(len(nums))}
        
        # num. of len(i) subarrays in len(nums):
        # len(nums) - len(i) + 1
        max_prod = max(nums)
        for subarray_len in range(2, len(nums) + 1):
            for i in range(len(nums) - subarray_len + 1):
                j = i + subarray_len
                prod = m[(i, j-1)] * nums[j-1]
                m[(i,j)] = prod
                max_prod = max(max_prod, prod)
        
        return max_prod
        
