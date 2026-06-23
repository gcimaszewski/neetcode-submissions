class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prfx_product = [1]
        reverse_prfx_product = [1]
        for idx in range(len(nums)):
            new_prod = nums[idx] * prfx_product[-1]
            prfx_product.append(new_prod)
            # reverse direction
            reverse_prfx_product.append(
                reverse_prfx_product[-1] * nums[len(nums) - 1 - idx]
            )
        
        output = []
        # output[i] = product(nums[:i]) * product(nums[i+1:])
        for idx in range(len(nums)):
            product = (
                prfx_product[idx] * 
            reverse_prfx_product[len(nums) - idx - 1]
            )
            output.append(product)
        return output
