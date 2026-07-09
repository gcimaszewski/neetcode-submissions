class Solution:
    """
    Multiply Strings

    You are given two strings num1 and num2 that represent non-negative integers.
    Return the product of num1 and num2 in the form of a string.
    Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.
    Note: You can not use any built-in library to convert the inputs directly into integers.
    """
    def multiply(self, num1: str, num2: str) -> str:        
        
        product = [0 for _ in range(len(num1) + len(num2))] # LSB is at index 0

        def addProductToRunningSum(summand, pow_10: int=0):
            carry = 0
            for i in range(len(product) - pow_10):
                if i < len(summand):
                    s = product[i + pow_10] + summand[i] + carry
                else:
                    s = product[i + pow_10] + carry
                product[i + pow_10] = s%10
                carry = s//10

        def multBySingleDigit(factor:str, lt10:str):
            prod = [0 for _ in range(len(factor) + 1)]
            carry = 0
            digit = int(lt10)
            for idx in range(len(factor)):
                p = int(factor[len(factor) - 1 - idx]) * digit +carry
                prod[idx] = p%10
                carry=p//10
            prod[len(factor)] = carry
            return prod

        if num1=="0" or num2=="0":
            return "0"

        longer = num1 if len(num1) > len(num2) else num2
        shorter = num2 if len(num2) < len(num1) else num1

        for pow_10, multiplier in enumerate(reversed(shorter)):
            one_row_prod = multBySingleDigit(longer, multiplier)
            running_sum = addProductToRunningSum(one_row_prod, pow_10)
        for i in range(len(product) - 1, 0, -1):
            if product[i] == 0:
                del product[i]
            elif product[i] > 0:
                break
        return "".join(reversed([str(d) for d in product]))
