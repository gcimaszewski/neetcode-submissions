class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sum_ =(digits[i] + carry )
            carry = sum_//10
            digits[i] = sum_%10
        if carry > 0:
            digits.insert(0, carry)
        return digits