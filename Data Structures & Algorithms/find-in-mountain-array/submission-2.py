class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        # Find the peak
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            a = mountainArr.get(mid - 1)
            b = mountainArr.get(mid)
            c = mountainArr.get(mid + 1)

            if b > a and b > c:
                # mid is the peak
                break
            elif a < b < c:
                # The peak is to the right
                l = mid + 1
            else:
                r = mid - 1

        peak = mid

        # Search the left portion
        l = 0
        r = peak - 1

        while l <= r:
            mid = l + (r - l) // 2
            guess = mountainArr.get(mid)

            if guess == target:
                return mid
            elif guess > target:
                r = mid - 1
            else:
                l = mid + 1

        # Search the right portion
        l = peak
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2
            guess = mountainArr.get(mid)

            if guess == target:
                return mid
            elif guess > target:
                # The right portion is in descending order
                # so we update l if the guess is too large.
                l = mid + 1
            else:
                r = mid - 1

        return -1
        