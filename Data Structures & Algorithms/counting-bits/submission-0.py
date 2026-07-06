class Solution:
    def countBits(self, n: int) -> List[int]:
        def get1bits(num):
            nbits = 0
            for i in range(32):
                nbits += num & 1
                num = num >> 1
                # div = 1 << i
                # nbits += div & num
            return nbits
        
        result = []
        for i in range(n+1):
            result.append(get1bits(i))
        return result