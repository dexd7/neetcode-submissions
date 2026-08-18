class Solution:
    def isValid(self, s: str) -> bool:
        checker_dict = { ')': '(', '}': '{', ']': '['}
        stack = []
        for bracket in s:
            if bracket not in checker_dict:
                stack.append(bracket)
            else:
                if stack:
                    if checker_dict[bracket] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                        
                else:
                    return False
        return not stack


            
        
        