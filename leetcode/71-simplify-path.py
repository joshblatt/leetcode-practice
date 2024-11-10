# O(n) time O(n) space
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for directory in path:
            if directory == '..':
                if stack:
                    stack.pop()
            elif directory and directory != '.':
                stack.append(directory)

        return "/" + "/".join(stack) if stack else '/'