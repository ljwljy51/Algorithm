# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val == val:
                return node
            if node.val < val:  # 현재 노드값보다 큰 값을 찾는 경우
                node = node.right
            else:
                node = node.left
        return None
