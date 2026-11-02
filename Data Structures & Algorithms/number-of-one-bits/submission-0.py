class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        c = 0
        for i in b:
            if i == '1':
                c += 1

        return c