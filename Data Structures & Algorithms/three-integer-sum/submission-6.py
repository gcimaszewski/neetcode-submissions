class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # approach:
        # 2sum + fix the third value (gives O(n^2))
        nums = sorted(nums)
        triplets = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            # num_to_idx = {}
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                # target = - (nums[idx] + nums[left])
                if total == 0:
                    triplets.append((nums[idx], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -=1
                elif total < 0 :
                    left += 1
                else:
                    right -= 1
            # for j in range(idx + 1, len(nums)):
            #     if j > idx + 1 and nums[j] == nums[j-1]:
            #         continue
            # # nums[j] = -nums[idx_fixed] -nums[i2]
            #     target = - nums[idx] - nums[j]
            #     if target in num_to_idx:
            #         triplets.append((nums[idx], nums[j], target))
            #   #      triplets.append((idx, j, num_to_idx[target]))
            #     num_to_idx[nums[j]] = j
            # num_to_idx.clear()    
        return triplets
