class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = {']': '[', '}': '{', ')': '('}
        stack = []
        for bracket in s:
            if bracket not in closing_brackets:
                stack.append(bracket)
            else:
                if stack:
                    temp = stack.pop()
                    if temp != closing_brackets[bracket]:
                        return False
                else:
                    return False
        return len(stack) == 0    
