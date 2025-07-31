class Solution:
    def reverse(self, x: int) -> int:

         res = 0
         negative = 1
         if x < 0:
             negative = -1
         x = abs(x)
         while x:
             temp = x % 10
             res = res * 10 + temp
             x = x // 10
         if res < -2 ** 31:
            return 0
         if res > 2**31 - 1:
             return 0
         return res * negative

if __name__ == "__main__":
    obj = Solution()
    print(obj.reverse(15342364))