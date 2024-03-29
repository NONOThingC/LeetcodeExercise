From https://leetcode.com/problems/network-delay-time/discuss/283711/Python-Bellman-Ford-SPFA-Dijkstra-Floyd-clean-and-easy-to-understand

Since the input is edges, it naturally occured to me to use Bellman-Ford. Of course we can process the edges and use SPFA (Shortest Path Faster Algorithm) and Dijkstra.

## Bellman-Ford
Time: O(VE)
Space: O(N)

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]
        dist[K-1] = 0
        for _ in range(N-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
        return max(dist) if max(dist) < float("inf") else -1
```
## SPFA
Time: average O(E), worst O(VE)
Space: O(V+E)

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]
        K -= 1
        dist[K] = 0
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u-1][v-1] = w
        queue = collections.deque([K])
        while queue:
            u = queue.popleft()
            for v in weight[u]:
                if dist[u] + weight[u][v] < dist[v]:
                    dist[v] = dist[u] + weight[u][v]
                    queue.append(v)
        return max(dist) if max(dist) < float("inf") else -1
```

## Dijkstra
Time: O(E+VlogV)
Space: O(V+E)
这个算法和上面的区别就是这个直接压到优先队列里面，没有把dist大的点排除掉。
```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        weight = collections.defaultdict(dict)#模板用字典表示邻接表，也可以考虑用正常的二维数组形式
        for u, v, w in times:
            weight[u][v] = w
        heap = [(0, K)]
        dist = {}
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in weight[u]:
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))
        return max(dist.values()) if len(dist) == N else -1
```

Floyd-Warshall
Time: O(V^3)
Space: O(V^2)

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            dist[u-1][v-1] = w
        for i in range(N):
            dist[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        return max(dist[K-1]) if max(dist[K-1]) < float("inf") else -1
```