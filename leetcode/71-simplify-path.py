# O(n) time O(n) space
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        new_path = ''
        for i in range(len(path)):
            if path[i] == '' or path[i] == '.':
                continue
            elif path[i] == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(path[i])
        for i in range(len(stack)):
            new_path += ('/' + stack[i])
        if len(new_path) == 0:
            new_path += '/'
        return new_path