class Solution:
    """
    You are given an integer n.
    Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        
        parens_strs = []
        state = []

        def backtrack(open_parens, closed_parens):
            # to generate a string:
            # we can either add a closed pair () to an existing valid string,
            # or open a new parens ( and close it later
            if open_parens == closed_parens == n:
                parens_strs.append("".join(state))
                return
            
            if open_parens < n:
                state.append("(")
                backtrack(open_parens + 1, closed_parens)
                state.pop()

            if closed_parens < open_parens and open_parens <= n:
                state.append(")")
                backtrack(open_parens, closed_parens + 1)
                state.pop()
        
        backtrack(0, 0)
        return parens_strs
