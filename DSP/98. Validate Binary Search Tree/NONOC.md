View some instance we could see:
![](%202020-09-23-11-20-06.png)

When we visit left tree, max(the A in figure) will be update,with right tree corresponding to min.

So:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dsp(root,min_val=float("-inf"),max_val=float("inf")):
            if not root:
                return True
            if root.left:
                if root.left.val<min(max_val,root.val) and root.left.val>min_val:
                    answer=dsp(root.left,min_val,min(max_val,root.val))
                    if not answer:
                        return False
                else:
                    return False
            if root.right:
                if root.right.val<max_val and root.right.val>max(min_val,root.val):
                    answer=dsp(root.right,max(min_val,root.val),max_val)
                    if not answer:
                        return False
                else:
                    return False
            return True
        answer=dsp(root)
        return answer
```

We see some symmetry between left and right, so we could do some optimize:
```python
class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))
```