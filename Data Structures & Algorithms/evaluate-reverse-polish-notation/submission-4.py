class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_dict = {'+', '*', '-', '/'}
        stack = []
        for ch in tokens:
            if ch not in valid_dict:
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()
                if ch == '+':
                    stack.append(a+b)
                elif ch == '*':
                    stack.append(a*b)
                elif ch == '-':
                    stack.append(a-b)
                elif ch == '/':
                    stack.append(int(a/b))
        return stack[-1]
                    