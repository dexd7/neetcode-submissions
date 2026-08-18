class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for val in tokens:
            if val not in operators:
                stack.append(int(val))
            else:
                b = stack.pop()
                a = stack.pop()
                if val == '+':
                    stack.append(a+b)
                if val == '-':
                    stack.append(a-b)
                if val == '*':
                    stack.append(a*b)
                if val == '/':
                    stack.append(int(a/b))
        return stack[-1]