class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp_dict = {')' : '(', '}':'{', ']': '['}
        for ch in s:
            if ch not in temp_dict:
                stack.append(ch)
            else:
                if not stack:
                    return False
                opener = stack.pop()
                if opener != temp_dict[ch]:
                    return False
        return not stack
        
        