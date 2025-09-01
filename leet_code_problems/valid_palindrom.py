class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(filter(str.isalnum, s))
        if not s:
            return True
        s = s.lower()
        return True if s == s[::-1] else False



if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome('A man, a plan, aww canal: Panama'))
