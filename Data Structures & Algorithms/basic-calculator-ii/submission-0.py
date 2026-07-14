class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        num = 0
        op ='+'
        for idx, char in enumerate(s):
            print(char)
            if char.isdigit():
                num = num*10 + int(char)
            if (not char.isdigit() and char != " ") or idx == len(s) - 1:
                if op== '+':
                    stack.append(num)
                elif op== '-':
                    stack.append(-num)
                elif op== '*':
                    stack.append(stack.pop()*num)
                elif op== '/':
                    stack.append(int(stack.pop()/num))
                num = 0
                op = char
        return sum(stack)