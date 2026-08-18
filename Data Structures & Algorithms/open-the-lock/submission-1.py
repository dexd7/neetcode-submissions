class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        visit = set(deadends)
        if '0000' in visit:
            return -1
        q = deque(["0000"])
        visit.add("0000")
        steps = 0
        while q:
            steps+=1
            for _ in range(len(q)):
                lock_val = q.popleft()
                for i in range(4):
                    for j in [-1,1]:
                        digit = str(((int(lock_val[i]))+j+10)%10)
                        next_lock_val = lock_val[:i] + digit + lock_val[i+1:]
                        if next_lock_val in visit:
                            continue
                        if next_lock_val == target:
                            return steps
                        q.append(next_lock_val)
                        visit.add(next_lock_val)
        return -1
        

