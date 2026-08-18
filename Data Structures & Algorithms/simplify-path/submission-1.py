class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = path.split('/')
        stack = []
        for word in temp:
            if word == '.' or word == '':
                continue
            elif word == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(word)
        return '/'+ '/'.join(stack)