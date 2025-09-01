from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor = xor ^ i

        return xor






if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNumber([2,2,1,3,4,4,3,5,5]))
