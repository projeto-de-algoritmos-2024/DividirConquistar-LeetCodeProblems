class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        n = len(l)
        if n%2 != 0:
            median = l[int(n/2)]
        else:
            b = int(n/2)
            a = b-1
            median = (l[a] + l[b]) / 2
        return median