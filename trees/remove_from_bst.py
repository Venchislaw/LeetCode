# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def min_node(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        else:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min_node = self.min_node(root.right)
                    root.val = min_node.val

                    root.right = self.deleteNode(root.right, min_node.val)
        return root
    