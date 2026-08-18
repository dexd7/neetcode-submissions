class Solution:
    def isValid(self, s: str) -> bool:
        bucket = {']': '[', '}': '{', ')': '('}
        stack = []
        for bracket in s:
            if bracket not in bucket:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if opening != bucket[bracket]:
                    return False
        return len(stack) == 0
