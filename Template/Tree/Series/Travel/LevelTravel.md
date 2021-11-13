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
```
pre = q
current = []
for p in q:
    for child in [p.left, p.right] :
        if child:
            current.append(child)
q = current

```
