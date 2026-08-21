class Solution:
    def isValid(self, s: str) -> bool:
        open_counterpart = { ')': '(', '}': '{', ']':'['}
        tracking_stack = []
        for bracket in s:
            if bracket not in open_counterpart:
                tracking_stack.append(bracket)
            else:
                if not tracking_stack:
                    return False
                if tracking_stack.pop() != open_counterpart[bracket]:
                    return False
        return len(tracking_stack) == 0
