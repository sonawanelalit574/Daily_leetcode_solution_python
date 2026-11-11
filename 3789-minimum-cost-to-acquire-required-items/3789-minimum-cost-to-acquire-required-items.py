class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, cost_both: int, need1: int, need2: int
    ) -> int:
        # Strategy A: buy every item individually, no bundles used.
        buy_individually = need1 * cost1 + need2 * cost2

        # Strategy B: cover both needs using only bundles.
        # Buying max(need1, need2) bundles satisfies both requirements,
        # since each bundle provides one of each type (surplus is acceptable).
        buy_only_bundles = cost_both * max(need1, need2)

        # Strategy C: use bundles for the overlapping (smaller) amount,
        # then fill the remaining items of the larger requirement individually.
        min_need = min(need1, need2)
        buy_mixed = (
            cost_both * min_need
            + (need1 - min_need) * cost1
            + (need2 - min_need) * cost2
        )

        # Return the cheapest of the three strategies.
        return min(buy_individually, buy_only_bundles, buy_mixed)
