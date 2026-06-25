class Solution:
    def isValid(self, s: str) -> bool:
        open_to_closed = {')': '(', '}': '{', ']': '['}

        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack:
                    return False
                pair = stack.pop()
                if pair != open_to_closed[char]:
                    return False
        
            else: 
                continue
        return len(stack) == 0