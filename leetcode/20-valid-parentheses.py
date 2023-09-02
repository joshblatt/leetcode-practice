class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else:
                    open_ch = stack.pop()
                    if (open_ch == '[' and ch != ']') or (open_ch == '(' and ch != ')') or (open_ch == '{' and ch != '}'):
                        return False
        return len(stack) == 0