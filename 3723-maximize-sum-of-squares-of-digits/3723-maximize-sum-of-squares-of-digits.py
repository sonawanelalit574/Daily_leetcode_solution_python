class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Guard clause MUST come first: the maximum achievable
        # digit sum with `num` digits is 9 * num.
        if num * 9 < sum:
            return ""

        quotient, remainder = divmod(sum, 9)
        result = "9" * quotient
        if remainder:
            result += str(remainder)
        result += "0" * (num - len(result))
        return result