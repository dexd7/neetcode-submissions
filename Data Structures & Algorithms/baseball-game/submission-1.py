class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch == '+':
                stack.append(stack[-1]+stack[-2])
            elif ch == 'D':
                stack.append(2*stack[-1])
            elif ch == 'C':
                stack.pop()
            else:
                stack.append(int(ch))
        return sum(stack)
