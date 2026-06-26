class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        last_temp = float('inf')
        # invariant: temperatures stored on stack are non-increasing
        stack = [(0, temperatures[0])]
        result_to_idx = {}
        for idx in range(1, len(temperatures)):
            temp = temperatures[idx]
            if not stack:
                stack.append((idx, temp))
            else:
                prev_idx, prev_temp = stack[-1]
                if temp <= prev_temp:
                    stack.append((idx, temp))
                else:
                    while temp > prev_temp:
                        last_idx, last_temp = stack.pop()
                        result_to_idx[last_idx] = (idx - last_idx)
                        if not stack:
                            break
                        _, prev_temp = stack[-1]
                    stack.append((idx, temp))
        
        # convert to final result
        result = []
        for i in range(len(temperatures)):
            warmer_idx = result_to_idx.get(i, 0)
            result.append(warmer_idx)
        return result