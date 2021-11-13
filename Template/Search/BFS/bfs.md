# BFS
```python
bfs = [target.val]
visited = set([target.val])
for k in range(K):
    bfs = [y for x in bfs for y in conn[x] if y not in visited]
    visited |= set(bfs)
return bfs
```

```python
import collections
def bfs(st_nd,tar_nd):
    queue=collections.deque(st_nd)
    visits=set(tar_nd)
    depth=0
    while queue:
        for i in range(len(queue)):
            cur=queue.pop()
            if cur==tar_nd:
                return step # any need information
            for j in i.neighbor():
                if j not in visits:
                    queue.append(j)
                    visits.add(j)
        depth+=1

```
