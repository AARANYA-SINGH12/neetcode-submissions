# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        stk = []
        cur = root 

        while stk or cur:
            if cur:
                res.append(cur.val)
                stk.append(cur.right)
                cur = cur.left
            else:
                cur = stk.pop()

        return res