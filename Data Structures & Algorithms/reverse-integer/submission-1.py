class Solution:
    def reverse(self, x: int) -> int:
        # approach:
        # get the highest order digit by repeatedly dividing by 10 until num < 10
        # add it to the accumulator
        # before adding: multiple accum by 10, to move to the next digit of the result

        res = 0
        sign = -1 if x < 0 else 1
        remainder = abs(x)
        overflow = 2**31 - 1
        underflow = -2**31
        while remainder > 0:
            # check for overflow
            lsd = remainder % 10
            if res > (overflow - lsd)//10:
                return 0
            # TODO: why is this?
            elif res <= (underflow + lsd)//10:
                return 0
            res = (res * 10) + sign * lsd
            remainder = (remainder - lsd)//10
        
        return res