class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_element = m+n-1
        m,n = m-1,n-1
        while (m>=0 and n>=0) and last_element>0:
            if nums1[m]>nums2[n]:
                nums1[last_element] = nums1[m]
                m-=1
            else:
                nums1[last_element] = nums2[n]
                n-=1
            last_element-=1
        while m>=0:
            nums1[last_element] = nums1[m]
            m-=1
            last_element-=1
        while n>=0:
            nums1[last_element] = nums2[n]
            n-=1
            last_element-=1