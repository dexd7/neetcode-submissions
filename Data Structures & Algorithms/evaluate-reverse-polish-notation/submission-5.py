class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_lookup_o1 = {'+', '-', '*', '/'}
        stack = []
        for ch in tokens:
            if ch not in operation_lookup_o1:
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()
                if ch == '+':
                    stack.append(a+b)
                elif ch == '-':
                    stack.append(a-b)
                elif ch == '*':
                    stack.append(a*b)
                elif ch == '/':
                    stack.append(int(a/b))
        return stack[-1]
