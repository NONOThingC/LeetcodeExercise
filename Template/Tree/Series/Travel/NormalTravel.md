```python
Pre, In, Post Iteratively Summarization
In preorder, the order should be

root -> left -> right

But when we use stack, the order should be reversed:

right -> left -> root

Pre
#原理就是把所有的遍历序列先生成好再逐步输出
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node: #注意这个要检测是不是空的情况！！！！
                if visited:  
                    res.append(node.val)
                else:  # preorder: root -> left -> right #注意这个次序是反的！！！！！
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res
In inorder, the order should be
left -> root -> right

But when we use stack, the order should be reversed:

right -> root -> left

In

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res
In postorder, the order should be
left -> right -> root

But when we use stack, the order should be reversed:

root -> right -> left

Post

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> right -> root
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res

```


```python
def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []
def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []
```
