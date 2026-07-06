class Solution:

    """
    Letter Combinations of a Phone Number

    You are given a string digits made up of digits from 2 through 9 inclusive.

    Each digit (not including 1) is mapped to a set of characters as shown below:

    A digit could represent any one of the characters it maps to.

    Return all possible letter combinations that digits could represent.
    You may return the answer in any order.
    """

    def letterCombinations(self, digits: str) -> List[str]:
        # this is a little similar to combination generation
        # each place in digits is a level in the decision tree
        # each path corresponds to one letter that digit maps to

        if len(digits) == 0:
            return []

        combs = []
        state = []

        digit_char_mapping = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        def backtrack(i):
            if i >= len(digits):
                combs.append("".join(state))
                return
            
            for char in digit_char_mapping[digits[i]]:
                state.append(char)
                backtrack(i+1)
                state.pop()
        
        backtrack(0)
        return combs
            # for each choice (e.g., possible letter mapping):
            #     add that choice to the current running mapping
            #     backtrack
            #     undo the choice to continue onto the next one