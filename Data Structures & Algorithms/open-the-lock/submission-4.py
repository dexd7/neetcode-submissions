class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0
        if target in deadends:
            return -1 
        visited = set(deadends)
        queue = deque()
        queue.append('0000')
        visited.add('0000')
        turns = 1
        while queue:
            for _ in range(len(queue)):
                passCode = queue.popleft()
                for i in range(len(passCode)):
                    for j in [1,-1]:
                        newDigit = str((int(passCode[i]) + j)%10)
                        newPasscode = passCode[:i] + newDigit + passCode[i+1:]
                        if newPasscode == target:
                            return turns
                        if newPasscode not in visited:
                            visited.add(newPasscode)
                            queue.append(newPasscode)
            turns+=1
        return -1