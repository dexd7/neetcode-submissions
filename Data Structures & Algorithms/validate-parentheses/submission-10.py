class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup_O1 = {']': '[', '}': '{', ')': '('}
        for ch in s:
            if ch not in lookup_O1:
                stack.append(ch)
            else:
                if stack:
                    last = stack.pop()
                    if last != lookup_O1[ch]:
                        return False
                else:
                    return False
        return len(stack) == 0