class Solution:
    def multiply(self, num1: str, num2: str) -> str:        
        
        
        def sumTwoStrs(n1, n2):
            sum_ = []
            carry=0
            for i in range(max(len(n1), len(n2))):
                digit1 = int(n1[len(n1) - 1 - i]) if i < len(n1) else 0
                digit2 = int(n2[len(n2) - 1 - i]) if i < len(n2) else 0
                s = digit1+digit2+carry
                sum_.append(str(s%10))
                carry = s//10
            if carry:
                sum_.append(str(carry))
            return "".join(reversed(sum_))

        def multBySingleDigit(factor:str, lt10:str, multby10:int):
            prod = ["0" for _ in range(multby10)]
            carry=0
            for idx in range(len(factor)):
                p = int(factor[len(factor) - 1 - idx]) * int(lt10) +carry
                prod.append(str(p%10))
                carry=p//10
            if carry: prod.append(str(carry))
            return "".join(reversed(prod))

        if num1=="0" or num2=="0":
            return "0"

        longer = num1 if len(num1) > len(num2) else num2
        shorter = num2 if len(num2) < len(num1) else num1

        running_sum = "0"
        for pow_10, multiplier in enumerate(reversed(shorter)):
            one_row_prod = multBySingleDigit(longer, multiplier, pow_10)
            running_sum = sumTwoStrs(running_sum, one_row_prod)
        return running_sum
