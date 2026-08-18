class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combinations = [[po,sp] for po,sp in zip(position,speed)]
        stack = []
        combinations.sort(reverse=True)
        for i in range(len(combinations)):
            time_req = (target-combinations[i][0])/combinations[i][1]
            stack.append(time_req)
            while len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
            
                
            