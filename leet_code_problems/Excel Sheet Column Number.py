class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        column_number = 0
        for i in columnTitle:
            temp_column_number = ord(i) - ord("A") + 1
            column_number = column_number*26+temp_column_number
        return column_number


if __name__=="__main__":
    obj =Solution()
    print(obj.titleToNumber('AA'))