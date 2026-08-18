class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens.pop())
        operators = {'+', '-', '*', '/'}
        a = 0
        b = 0
        stack = []
        for thingamajing in tokens:
            if thingamajing not in operators:
                stack.append(thingamajing)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if thingamajing == '+':
                    stack.append(a+b)
                elif thingamajing == '-':
                    stack.append(a-b)
                elif thingamajing == '*':
                    stack.append(a*b)
                elif thingamajing == '/':
                    stack.append(int(a/b))
        return stack.pop()


