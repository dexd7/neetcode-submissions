class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                word = ''
                while stack and stack[-1] != '[':
                    word=stack.pop()+word
                stack.pop()
                length = ''
                while stack and stack[-1].isdigit():
                    length=stack.pop()+length
                stack.append(word*int(length))
            else:
                stack.append(ch)
        return ''.join(stack)