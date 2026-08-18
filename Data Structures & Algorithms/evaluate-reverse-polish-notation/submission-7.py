class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        eval_RPN = []
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                eval_RPN.append(int(tokens[i]))
            else:
                b = eval_RPN.pop()
                a = eval_RPN.pop()
                if tokens[i] == '+':
                    eval_RPN.append(a+b)
                elif tokens[i] == '-':
                    eval_RPN.append(a-b)
                elif tokens[i] == '*':
                    eval_RPN.append(a*b)
                elif tokens[i] == '/':
                    eval_RPN.append(int(a/b))
        return eval_RPN[-1]
