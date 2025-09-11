from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(numbers)):
            temp = target - numbers[i]

            if numbers[i] in list(res.keys()):
                return [res[numbers[i]] + 1, i+ 1]

            else:
                res[temp] = i
        return []

if __name__ == "__main__":
    obj = Solution()
    print(obj.twoSum(numbers = [-1,0], target = -1))