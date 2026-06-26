class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row_idx = -1
        r_row_idx = len(matrix)
        # first, find the row where target would fit into
        # get the row after the last row where row[-1] < target
        while l_row_idx + 1 < r_row_idx: 
            mid = l_row_idx + (r_row_idx - l_row_idx)//2
            if matrix[mid][-1] < target:
                l_row_idx = mid
            else:
                r_row_idx = mid
        # right should contain the row that we want
        # do a safety check: 
        if r_row_idx == len(matrix):
            return False
        row_to_search = matrix[r_row_idx]
        if row_to_search[0] > target:
            return False
        left = -1
        right = len(row_to_search)
        while left + 1 < right:
            mid = left + (right-left)//2
            if row_to_search[mid] >= target:
                right = mid
            else:
                left = mid
        if right < len(row_to_search) and row_to_search[right]==target:
            return True
        else:
            return False