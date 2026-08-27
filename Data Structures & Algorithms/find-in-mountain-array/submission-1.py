class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #finding peak point of the array:
        l = 0 
        r = mountainArr.length()-1
        peak = 0
        while l<r:
            m = l+(r-l)//2
            if mountainArr.get(m)<mountainArr.get(m+1):
                l = m+1
            else:
                r = m
        peak = r
        #searching left
        l, r = 0, peak
        while l<=r:
            m = l+(r-l)//2
            if mountainArr.get(m)>target:
                r = m-1
            elif mountainArr.get(m)<target:
                l = m+1
            else:
                return m
        #searching right
        l, r = peak+1, mountainArr.length()-1
        while l<=r:
            m = l+(r-l)//2
            if mountainArr.get(m)>target:
                l = m+1
            elif mountainArr.get(m)<target:
                r = m-1
            else:
                return m
        return -1