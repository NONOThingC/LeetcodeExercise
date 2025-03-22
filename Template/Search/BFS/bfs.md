

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
def BFS(start, target):
    queue = collections.deque([start])     # 核心数据结构-队列
    visited = set(start)                 # 记录走过的路径，避免走回头路--使用集合，检索速度更快
    # queue.append(start)
    # visited.add(start)
    step = 0                        # 记录扩散的步数
    while queue:
        size = len(queue)           # 将当前队列中的所有节点向四周扩散
        for i in range(size):       # 每次把当前队列中
            cur = queue.popleft()
            if cur == target:
                return step
            for node in cur:        # 将cur的相邻节点加入队列
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
        step += 1
    return step
```
