class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        i = 0
        is_negative = False
        res = 0
        if not s:
            return res
        if s[0] == "-":
            is_negative = True
            i = 1
        if s[0] == "+":
            i = 1
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        if is_negative:
            res = res - (res * 2)
            if res < -2 ** 31:
                return -2 ** 31
            else:
                return res
        else:
            if res > (2 ** 31) - 1:
                return (2 ** 31) - 1
            else:
                return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.myAtoi("+1"))