class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        close_parantheses = close_to_open.keys()

        for c in s:
            if c in close_parantheses:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if close_to_open[c] != top:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
