class Solution:
    def checkValidString(self, s: str) -> bool:
        # at no point can 
        open_stack = []
        star_stack = []
        for i in range(len(s)):
            match s[i]:
                case "(":
                    open_stack.append(i)
                case "*":
                    star_stack.append(i)
                case ")":
                    if len(open_stack) == 0:
                        # try converting a star into an open parens
                        try:
                            star_stack.pop()
                        except IndexError:
                            return False
                    else:
                        _ = open_stack.pop()
        #print(f'{len(open_stack)}. {len(star_stack)}')
        while len(open_stack) > 0 and len(star_stack) > 0:
            # if we have any stars left, convert them to closed parens
            last_open_parens = open_stack[-1]
            idx = star_stack.pop()
            if idx > last_open_parens:
                _ = open_stack.pop()

        return len(open_stack) == 0