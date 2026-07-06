class Solution:
    """
    Given two integers a and b, return the sum of the two integers without using the + and - operators.
    """
    def getSum(self, a: int, b: int) -> int:
        # for bitwise addition:
        # carry is set if both a, b are 1 => carry=a&b
        # add is0 if same, 1 if different => place = a^b
        if a==0:
            return b
        elif b==0:
            return a
        sum_ = 0
        carry = 0
        for i in range(32):
            bit_here = (a ^ b ^ carry) & 1
            sum_ += (bit_here << i)
            carry = ((a & b) | (a & carry) | (b & carry)) & 1
            a >>= 1
            b >>= 1
        # the problem here is that `sum_` is a standard 64-bit python int
        # even if we have a -1 at the end (negative), this gets represented as a large positive int
        # solution: AND with a 32-bit bitmask
        twos_comp = 0
        msb = sum_ & (1 << 31)
        print(f'msb: {msb}')
        sum_orig = sum_
        if msb: # need to convert to positive, then negate
            for b in range(32):
                flipped_bit = (sum_ & 1) ^ 1
                twos_comp += flipped_bit << b
                sum_ >>= 1
            return -(twos_comp + 1)
        return sum_
        if carry and sum_:
            return sum_ | (0xffffffff << 32)
        else:
            return sum_