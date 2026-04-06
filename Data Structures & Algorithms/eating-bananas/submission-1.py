class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            mid = (l+r) // 2

            totalHours = 0

            for p in piles:
                totalHours += math.ceil(float(p)/mid)
            if  totalHours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res