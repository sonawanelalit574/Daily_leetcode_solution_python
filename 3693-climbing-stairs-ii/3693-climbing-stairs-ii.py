class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Use the length of costs as the total number of stairs
        num_stairs = len(costs)

        # dp[i] represents the minimum total cost to reach stair i
        # Initialize all values to infinity, except the starting point (ground, stair 0)
        dp = [inf] * (num_stairs + 1)
        dp[0] = 0

        # Iterate over each stair (1-indexed) along with its cost
        for i, cost in enumerate(costs, 1):
            # From stair j, we can jump to stair i if i - j is at most 3,
            # so consider the three previous positions: i-3, i-2, i-1
            for j in range(i - 3, i):
                # Make sure the previous position is valid (not below ground)
                if j >= 0:
                    # Transition: cost to reach j, plus the cost of stair i,
                    # plus the squared distance penalty (i - j)^2
                    dp[i] = min(dp[i], dp[j] + cost + (i - j) ** 2)

        # The answer is the minimum cost to reach the top stair
        return dp[num_stairs]
