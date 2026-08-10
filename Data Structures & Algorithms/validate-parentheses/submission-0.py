class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {
                ')' : '(', 
                '}' : '{',
                ']' : '['
            }

        for i in s:
            if i in d:
                if stk and stk[-1] == d[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)

        return True if not stk else False