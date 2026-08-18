class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        if '0000' in visit:
            return -1
        visit.add('0000')
        q = deque()
        q.append('0000')
        total_turns = 0
        while q:
            total_turns+=1
            for _ in range(len(q)):
                cur_lock = q.popleft()
                for i in range(4):
                    for j in [-1,1]:
                        digit = str((int(cur_lock[i])+j)%10)
                        next_lock = cur_lock[:i]+digit+cur_lock[i+1:]
                        if next_lock in visit:
                            continue
                        if next_lock == target:
                            return total_turns
                        q.append(next_lock)
                        visit.add(next_lock)
        return -1
        