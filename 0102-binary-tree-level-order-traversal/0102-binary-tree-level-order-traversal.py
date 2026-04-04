# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        Q = deque([root])

        while Q:
            s = len(Q)
            curr_level = []

            for _ in range(s):
                node = Q.popleft()
                curr_level.append(node.val)

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            res.append(curr_level)
        return res
