# 注意点
图问题注意几个点：
以这段代码为例，首先是
1. 是不是图搜索，如果是代表节点只访问一次，那么visited数组就得确定好；
2. 然后确定是DFS还是BFS，相应的数据结构就是栈或者队列。
3. 确定是单向图还是双向图，以及节点是从0还是1开始。
4. 确定答案的更新位置是邻接外还是内：
    - 邻接外做判断时是后判断，代表了
    - 邻接内做判断时是先判断，但可能会遗漏初始点的判断。
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
