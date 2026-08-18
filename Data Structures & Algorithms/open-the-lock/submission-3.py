class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if target in visited:
            return -1
        if '0000' in deadends:
            return -1
        q = deque()
        visited.add('0000')
        q.append('0000')
        turns = 1
        while q:
            for _ in range(len(q)):
                curr_pass = q.popleft()
                for i in range(4):
                    digit = int(curr_pass[i])
                    for j in [-1,1]:
                        newDigit = (digit+j)%10
                        new_pass = curr_pass[:i] + str(newDigit) + curr_pass[i+1:]
                        if new_pass == target:
                            return turns
                        if new_pass in visited:
                            continue
                        q.append(new_pass)
                        visited.add(new_pass)
            turns+=1
        return -1
