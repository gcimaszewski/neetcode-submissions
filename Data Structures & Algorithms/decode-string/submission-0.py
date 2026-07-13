class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        k = 0
        previous_str = []
        for i in s:
            if i.isdigit():
                k = k*10 + int(i)
            elif i == '[':
                stack.append(("".join(previous_str), k))
                previous_str.clear()
                k = 0
            elif i == ']':
                last_str, k_factor= stack.pop()
                new_str = list(last_str) + k_factor*previous_str
                previous_str.clear()
                previous_str.extend(new_str)

            else:
                previous_str.append(i)
        return "".join(previous_str)
