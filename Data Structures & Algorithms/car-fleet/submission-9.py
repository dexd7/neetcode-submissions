class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_arr = [(po,sp) for po, sp in zip(position, speed)]
        car_groups = []
        combined_arr.sort(reverse=True)
        for i in range(len(combined_arr)):
            time_required = (target-combined_arr[i][0])/combined_arr[i][1]   
            if car_groups and time_required<=car_groups[-1]:
                continue
            car_groups.append(time_required)
        return len(car_groups) 
            
                           