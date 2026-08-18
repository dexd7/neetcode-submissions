class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = [(po, sp) for po,sp in zip(position, speed)]
        temp.sort(reverse=True)
        stack = []
        for i in range(len(temp)):
            time = (target-temp[i][0])/temp[i][1]
            stack.append(time)
            while len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
