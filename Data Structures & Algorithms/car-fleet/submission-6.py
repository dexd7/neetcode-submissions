class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #target = 10, position = [1,4], speed = [3,2]
        # we sort by position then speed and then we can pop the cars that catch up and keep the minimum speed at every point.
        time_calculator = [(po,sp) for po,sp in zip(position,speed)]
        fleetCount = [] # [time_required to reach the end.]
        #where time required = (target-position)/speed
        time_calculator.sort(reverse=True)
        for po,sp in time_calculator:
            time_required = (target-po)/sp
            if fleetCount and time_required<=fleetCount[-1]:
                continue
            fleetCount.append(time_required)
        return len(fleetCount)