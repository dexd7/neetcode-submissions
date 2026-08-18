class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(po, sp) for po, sp in zip(position,speed)]
        fleetCounter = []
        combined.sort(reverse=True, )
        for i in range(len(combined)):
            time_required = (target-combined[i][0])/combined[i][1]
            if fleetCounter and time_required<=fleetCounter[-1]:
                continue
            fleetCounter.append(time_required)
        return len(fleetCounter)