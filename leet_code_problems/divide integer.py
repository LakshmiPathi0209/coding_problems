class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        is_negative = False
        res = 0
        if divisor < 0 or dividend<0:
            is_negative =True
        divisor = abs(divisor)
        dividend = abs(dividend)
        while dividend >= divisor:
            res += 1
            dividend -= divisor

        if is_negative:
            return res - res * 2
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.divide(7, -3))