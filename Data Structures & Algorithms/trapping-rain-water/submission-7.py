class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        lmax = height[l]
        rmax = height[r]
        trapped_water = 0
        while l<r:
            if lmax<rmax:
                l+=1
                lmax= max(lmax,height[l])
                trapped_water += lmax-height[l]
            else:
                r-=1
                rmax= max(rmax,height[r])
                trapped_water += rmax-height[r]
        return trapped_water


