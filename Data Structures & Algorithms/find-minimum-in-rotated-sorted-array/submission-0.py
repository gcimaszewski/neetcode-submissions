class Solution:
    """
    You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.
    Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

    Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

    A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
    """

    def findMin(self, nums: List[int]) -> int:
        
        # new index = (index + num. rotations) % len(nums)
        # naive implementation:
        # iterate through the array, and find the first index where nums[i] > nums[idx+1]

        # trick: for the interval we have, check left, mid, right
        # if nums[mid] < nums[right]: that side is ok
        # invariant: nums[i] >= pivot for all i >= right
        # answer is nums[right]
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[-1]:
                left = mid
            else:
                right = mid
        return nums[right]