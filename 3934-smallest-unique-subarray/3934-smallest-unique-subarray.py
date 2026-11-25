
from typing import List, Dict


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        base = 19
        mod = 10**9 + 7

        powers = [1] * (n + 1)

        for i in range(1, n + 1):
            powers[i] = (powers[i - 1] * base) % mod

        def check(k):
            counts = {}

            h = 0
            for i in range(k):
                h = (h * base + nums[i]) % mod

            counts[h] = 1

            for i in range(1, n - k + 1):
                left = (powers[k - 1] * nums[i - 1]) % mod
                h = (h - left) % mod
                h = (h * base + nums[i + k - 1]) % mod

                counts[h] = counts.get(h, 0) + 1

            return any(v == 1 for v in counts.values())

        low, high = 1, n
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
