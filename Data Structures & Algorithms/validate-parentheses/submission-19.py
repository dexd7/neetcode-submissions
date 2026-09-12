class Solution:
    def isValid(self, s: str) -> bool:
        matching_open_bracket = {']': '[', '}':'{', ')': '('}
        stack = []
        for brack in s:
            if stack:
                if brack in matching_open_bracket:
                    if matching_open_bracket[brack] != stack.pop():
                        return False
                else:
                    stack.append(brack)
            else:
                if brack in matching_open_bracket:
                    return False
                else:
                    stack.append(brack)
        return True if len(stack) == 0 else False