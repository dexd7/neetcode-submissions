class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        total_water = 0
        while l<r:
            if lmax<rmax:
                l+=1
                lmax = max(lmax,height[l])
                total_water+=lmax-height[l]
            else:
                r-=1
                rmax=max(rmax,height[r])
                total_water+=rmax-height[r]
        return total_water

