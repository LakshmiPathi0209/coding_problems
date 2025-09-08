class Solution:
    def convert(self, s: str, numRows: int) -> str:

        lines = dict((row, "") for row in range(numRows))

        row, direction = 0, 1
        for c in s:
            lines[row] = lines[row] + c
            row += direction
            if row >= numRows:
                row = max(0, row - 2)
                if row != 0:
                    direction = -1
            elif row <= 0:
                direction = 1

        return ''.join(lines[row] for row in range(numRows))

if __name__ == "__main__":
    obj = Solution()
    print(obj.convert("PAYPALISHIRING", 3))