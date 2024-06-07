class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root) -> bool:
        row = [root]
        level = 0
        if root.val % 2 == 0: return False
        while any(row):
            level += 1
            row = [kid for node in row for kid in (node.left, node.right) if kid]
            if level % 2 == 0:
                if row[0].val % 2 == 0: return False
                for i in range(1, len(row)):
                    if row[i].val % 2 == 0: return False
                    if row[i-1].val >= row[i].val: return False

            else:
                if row[0].val % 2 == 1: return False
                for i in range(1, len(row)):
                    if row[i].val % 2 == 1: return False
                    if row[i-1].val <= row[i].val: return False
        
        return True
    
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(7)
sol = Solution()
print(sol.isEvenOddTree(root))