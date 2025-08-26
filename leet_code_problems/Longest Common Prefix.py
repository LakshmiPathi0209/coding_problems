from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        max_len = min([len(x) for x in strs])
        res_str = ''
        for i in range(max_len):
            temp = strs[0][i]
            if all([True if x[i] == temp else False for x in strs]):
                res_str = res_str + temp
            else:
                return res_str
        return res_str

if __name__ == "__main__":
    obj = Solution()
    print(obj.longestCommonPrefix(["flower","flow","floight"]))