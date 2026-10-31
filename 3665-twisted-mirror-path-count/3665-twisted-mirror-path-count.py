
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        m, n = len(grid), len(grid[0])

        # right[i][j]: ways entering cell while moving right
        # down[i][j]: ways entering cell while moving down
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # Start from (0, 0)
        right[0][0] = 1
        down[0][0] = 1

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    # Initial cell: choose right or down
                    if j + 1 < n:
                        right[0][1] = 1
                    if i + 1 < m:
                        down[1][0] = 1
                    continue

                r = right[i][j]
                d = down[i][j]

                if grid[i][j] == 1:
                    # Entered mirror moving right -> move down
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + r
                        ) % MOD

                    # Entered mirror moving down -> move right
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + d
                        ) % MOD

                else:
                    # Empty cell: continue in either direction
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + r + d
                        ) % MOD

                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + r + d
                        ) % MOD

        return (right[m - 1][n - 1] +
                down[m - 1][n - 1]) % MOD
