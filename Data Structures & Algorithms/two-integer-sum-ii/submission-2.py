class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # naive solution:
        # for each num: traverse array to find target - num
        # solution: use two pointers at each end of `numbers`
        # while n1 + n2 > target: decrement right pointer
        # while n1 + n2 < target: increment left pointer
        # we can remove swathes of the search space by using the non-decreasing ordered property
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
        return []
