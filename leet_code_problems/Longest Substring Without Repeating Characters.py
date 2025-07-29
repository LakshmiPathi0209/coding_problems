class Solution:
    def lengthOfLongestSubstring(self, s: str):
        start = 0
        step = 0
        res_str = ""
        len_res_str = 0
        temp = ''

        while start < len(s) and step<len(s):
            if s[step] in temp:
                if len(temp)>len(res_str):
                    res_str = temp
                    len_res_str = len(res_str)
                start = start + 1
                step = start
                temp = ''
            else:
                temp = temp + s[step]
                step = step + 1
        return max(len_res_str, len(temp))

if __name__ == "__main__":
    obj = Solution()
    print(obj.lengthOfLongestSubstring('aab'))
