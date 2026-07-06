class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for b in range(32):
            bit_here = n & 1
            result += bit_here << (31 - b)
            n >>= 1
        return result