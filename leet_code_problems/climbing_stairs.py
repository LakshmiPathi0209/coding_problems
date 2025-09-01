class Solution:
    def climbStairs(self, n: int) -> int:

        if n in [0, 1]:
            return n

        prev, prev1, i = 0, 1, 1
        cur = 0
        while i <= n:
            cur = prev1 + prev
            prev, prev1 = prev1, cur
            i+=1
        return cur


if __name__ == "__main__":
    obj = Solution()
    print(obj.climbStairs(2))