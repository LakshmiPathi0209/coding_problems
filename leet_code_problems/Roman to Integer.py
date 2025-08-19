class Solution:
    def romanToInt(self, s: str) -> int:
        integer_roman_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        res = 0
        arr_len = len(s)
        while i < arr_len:
            if i +1 < arr_len and integer_roman_mapping[s[i]] <  integer_roman_mapping[s[i+1]]:
                res = res - integer_roman_mapping[s[i]]
            else:
                res = res + integer_roman_mapping[s[i]]
            i = i+1
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("MCMXCIV"))

