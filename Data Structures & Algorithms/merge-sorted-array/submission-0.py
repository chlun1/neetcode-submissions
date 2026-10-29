class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        aux = nums1[:m]
        j, k = 0, 0

        for i in range(n + m):
            if k < m and j < n:
                if aux[k] < nums2[j]:
                    nums1[i] = aux[k]
                    k += 1
                else:
                    nums1[i] = nums2[j]
                    j += 1
            elif k < m:
                nums1[i] = aux[k]
                k += 1
            elif j < n:
                nums1[i] = nums2[j]
                j += 1
