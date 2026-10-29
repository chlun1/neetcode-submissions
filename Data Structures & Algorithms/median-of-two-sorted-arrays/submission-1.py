class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        total = len(nums1) + len(nums2)
        half = (total // 2) + 1
        prev = curr = 0

        while True:
            prev = curr
            n1 = nums1[i] if i < len(nums1) else float("inf")
            n2 = nums2[j] if j < len(nums2) else float("inf")

            if n1 < n2:
                curr = n1
                i += 1
            else:
                curr = n2
                j += 1

            if i + j == half:
                if total % 2:
                    return curr
                else:
                    return (prev + curr) / 2
        