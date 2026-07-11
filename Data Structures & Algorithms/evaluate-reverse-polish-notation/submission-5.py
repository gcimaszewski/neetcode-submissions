class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        print(" ".join(tokens))
        for tkn in tokens:
            if tkn in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                match tkn:
                    case '+':
                        stack.append(op1+op2)
                    case '-':
                        stack.append(op1-op2)
                    case '*':
                        stack.append(op1*op2)
                    case '/':
                        stack.append(int(op1/op2))
            else:
                stack.append(int(tkn))
            print(stack)
            # 10 6 9 3 + -11 * / *
        return stack.pop()
