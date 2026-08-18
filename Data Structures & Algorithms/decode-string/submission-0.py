class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                word = ''
                while stack and stack[-1] != '[':
                    word+=stack.pop()
                word = word[::-1]
                stack.pop()
                times = ''
                while stack and stack[-1].isdigit():
                    times += stack.pop()
                times = int(times[::-1])
                for i in range(len(word)*times):
                    stack.append(word[(i%len(word))])
            else:
                stack.append(ch)
        return ''.join(stack)