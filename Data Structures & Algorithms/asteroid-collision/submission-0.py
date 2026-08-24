class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            while stk and a < 0 and stk[-1] > 0:
                dif = a + stk[-1]
                if dif > 0:
                    a = 0
                elif dif < 0:
                    stk.pop()
                else:
                    stk.pop()
                    a = 0

            if a:
                stk.append(a)

        return stk