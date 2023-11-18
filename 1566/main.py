class Solution:
    @staticmethod
    def is_palin(s):
        n = len(s)
        off = 1 if n & 1 else 0
        return s[:n//2] == s[n//2+off:][::-1]

    def longest_palindromic_substring(self, s):
        if len(s) == 0: 
            raise ValueError("Length of string must be > 1")

        res = ""

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                pot = s[i:j]
                # print(f"{pot}: {len(pot)} <-> {len(res)} and {self.is_palin(pot)}")
                if len(pot) > len(res) and self.is_palin(pot):
                    res = pot

        return res

sol = Solution()
print(sol.longest_palindromic_substring("banana"))


