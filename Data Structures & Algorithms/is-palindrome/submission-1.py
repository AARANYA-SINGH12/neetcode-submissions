class Solution:
    def alphanum(self, i):
        return (ord('A') <= ord(i) <= ord('Z') or
                ord('a') <= ord(i) <= ord('z') or
                ord('0') <= ord(i) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while r > l and not self.alphanum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1

        return True