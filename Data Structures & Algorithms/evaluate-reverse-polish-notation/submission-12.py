class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'*', '+', '-', '/'}
        RPN_stack = []
        for token in tokens:
            if token in operators:
                if RPN_stack:
                    b = RPN_stack.pop()
                    a = RPN_stack.pop()
                    if token == '*':
                        RPN_stack.append(a*b)
                    elif token == '/':
                        RPN_stack.append(int(a/b))
                    elif token == '+':
                        RPN_stack.append(a+b)
                    elif token == '-':
                        RPN_stack.append(a-b)
                else:
                    raise TypeError("Need a number before we perform an operation!")
            else:
                RPN_stack.append(int(token))
        return RPN_stack[-1]