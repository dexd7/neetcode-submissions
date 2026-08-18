class Solution:
    def isValid(self, s: str) -> bool:
        matching_bracket = {')':'(',  ']':'[', '}':'{'} 
        stack = []
        for ch in s:
            if ch not in matching_bracket:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack.pop()!= matching_bracket[ch]:
                    return False
        return len(stack) == 0