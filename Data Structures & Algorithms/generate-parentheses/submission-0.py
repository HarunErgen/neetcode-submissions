class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        subresult = []

        def bt(state, o, c):
            if o > c: return
            if len(state) == n * 2:
                result.append(state)
                return
            
            if o > 0:            
                bt(state + "(", o - 1, c)
            if o != c and c > 0:
                bt(state + ")", o, c - 1)
        
        bt("", n, n)
        return result

