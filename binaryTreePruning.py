# leetcode 814
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def checkPrune(root):
    if root == None:
        return True
    left = checkPrune(root.left)
    right = checkPrune(root.right)
    if left:
        root.left = None
    if right:
        root.right = None
    return root.val == 0 and left and right
l = checkPrune(root)
if l:
    return None
return root
