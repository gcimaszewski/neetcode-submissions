class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach: sliding window algorithm
        # initialize left, right to be equal (single element)
        # expand rightward: when different element found, 
        # switch left = right and keep going
        # longest_len = 0
        # left, right = 0, 0
        # while left < len(nums) and right < len(nums):
        #     if nums[right] - nums[left] == (right - left):
        #         right += 1
        #     else:
        #         left = right
        #     substr_len = right - left + 1
        #     longest_len = max(longest_len, substr_len)
        # return longest_len
        # wrong wrong wrong - misread question

        # store each set
        union_sets = []
        num_to_set = {}
        seen = set(nums)
        max_set_size = 0
        # if this number+-1 is in `seen`, then we can form a set
        # how to keep track of these sets?
        # keep a table of numbers that are in a set : set number 
        # keep sets in an array
        # a number is a start of a consecutive set ONLY IF number - 1 DNE in array
        set_starts = []
        for num in nums:
            if num -1 not in seen:
                set_starts.append(num)
        for num in set_starts:
            set_size = 1
            counter = num + 1
            while counter in seen:
                set_size += 1
                counter += 1
            max_set_size = max(max_set_size, set_size)
        return max_set_size
            

        # for num in nums:
        #     if num-1 in seen:
        #         if (set_num := num_to_set.get(num - 1) ) is None:
        #             # this number isn't included in a set yet
        #             # make one and add both to it
        #             new_set = {num - 1, num}
        #             set_idx = len(union_sets)
        #             num_to_set[num - 1] = set_idx
        #             num_to_set[num] = set_idx
        #             union_sets.append(new_set)
        #         else:
        #             union_sets[set_idx].add(num)
        #             num_to_set[num] = set_idx
        #     seen.add(num)
        
        # now we have to squish the sets already formed



