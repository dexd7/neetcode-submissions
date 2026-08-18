class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = { ']': '[', '}': '{', ')': '('}
        stack = []
        for b in s:
            if b not in valid_dict:
                stack.append(b)
            else:
                if stack:
                    if valid_dict[b] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0

            
        
        