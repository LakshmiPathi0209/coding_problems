class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}
        i = 0
        while i < len(s):

            s_char = s[i]
            if s_count.get(s_char, None):
                s_count[s_char] = s_count[s_char] + 1
            else:
                s_count[s_char] = 1

            t_char = t[i]
            if t_count.get(t_char, None):
                t_count[t_char] = t_count[t_char] + 1
            else:
                t_count[t_char] = 1

            i += 1

        for i, j in s_count.items():

            if t_count[i] != j:
                return False
        return True

if __name__ == "__main__":
    obj = Solution()
    print(obj.isAnagram(s = "anagram", t = "nagaram"))