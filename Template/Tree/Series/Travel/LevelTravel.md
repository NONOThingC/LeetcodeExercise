Python:
```python

    def deepestLeavesSum(self, root):
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)
```

```
[child for p in q for child in [p.left, p.right] if child]
```
实际上就是
```python
q=[]
if root:
    q.append(root)

while q:
    current=[]
    for p in q:
        current = []
        for child in [p.left, p.right] :
            if child:
                current.append(child)
    q = current

```

leetcode 515:
```python
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        q=[]
        self.ans=[]
        if root:
            q.append(root)
            self.ans.append(root.val)
       
        while q:
            current = []
            level_max=-float("inf")
            for p in q:
                for child in [p.left,p.right]:
                    if child:
                        current.append(child)
                        level_max=max(level_max,child.val)
            q=current
            if level_max !=-float("inf"):
                self.ans.append(level_max)
        return self.ans
```


```python
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_tree(root, result):
    if not root:
        return
    # 这里借助python的双向队列实现队列
    # 避免使用list.pop(0)出站的时间复杂度为O(n)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        # do somethings
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(9)
    tree.right = TreeNode(0)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(1)

    print(level_order_tree(tree, []))
    # [4, 9, 0, 5, 1]

```
