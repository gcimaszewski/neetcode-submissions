class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        for _ in range(32):
            num_ones += (n & 1)
            n = n >> 1
        return num_ones