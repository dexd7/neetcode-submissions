class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = path.split('/')
        for entity in temp:
            if entity == '' or entity == '.':
                continue
            elif entity == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(entity)
        return '/' + '/'.join(stack)
            
