class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def bt(strt, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(strt, n + 1):
                comb.append(i)
                bt(i + 1, comb)
                comb.pop()

        bt(1, [])

        return res