C++:
```C++
class Union_Find{
public:
    Union_Find (int N) {
        for (int i = 0; i < N; i++) {
            id.push_back(i);
            sz.push_back(1);
        }
    }

    void Union(int A, int B) {
        int rootA = Find(A);
        int rootB = Find(B);
        if (rootA == rootB) return;
        if (sz[rootA] < sz[rootB]) {
            id[rootA] = rootB;
            sz[rootB] += sz[rootA];
        } else {
            id[rootB] = rootA;
            sz[rootA] += sz[rootB];
        }
    }

    int Find(int p) {
        while (p != id[p]) {
            id[p] = id[id[p]];
            p = id[p];
        }
        return p;
    }

    int maxSize() {
        int res = 0;
        for (auto s : sz)
            res = max(res, s);
        return res;
    }
    
private:
    vector<int> id;
    vector<int> sz;
};
```

python:
```python
class UnionFind():
    def __init__(self,N):
        self.par=list(range(N))
        self.rank=[0]*N

    def find_root(self,x):
        # Attention: just modify parent node to parent of parent node, not root node.
        while(self.par[x]!=x):
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return x
        """
        # modify parent node to root node
        if(par[x]==x):
            return x
        else:
            return par[x]=find_root(par[x])
        """
    def unite(self,x,y):
        """
        x union y
        """
        x_root=self.find_root(x)
        y_root=self.find_root(y)
        if(x_root==y_root):
            return

        if(self.rank[x]<=self.rank[y]):
            self.par[x]=y
            self.rank[y]+=self.rank[x]
        else:
            self.par[y]=x
            self.rank[x]+=self.rank[y]
            
    def max_rank():
        return max(self.rank)

    
    def same(self,x,y):
        """
        verify if x,y is in same set.
        """
        return self.find_root(x)==self.find_root(y)



```

java:

```java
class Solution {
    HashMap<Integer, Integer> map  = new HashMap<Integer, Integer>();

    int maxSize = 1;
    int[] size; // the size of the each component.
    int[] parent; // the parent of each element.
    public int longestConsecutive(int[] nums) {
        int len = nums.length;
        if(len == 0) return 0;
        parent = new int[len];
        size = new int[len];
        Arrays.fill(size,1);
        for(int i = 0;i < len;i++) {
           if(map.containsKey(nums[i])){
                continue;
            }
            map.put(nums[i], i);
            parent[i] = i;
            if(map.containsKey(nums[i] - 1)){
                unite(i, map.get(nums[i] - 1));
            }
            if(map.containsKey(nums[i] + 1)){
                unite(i, map.get(nums[i] + 1));
            }
        }
        return maxSize;
    }

    public int find(int x) {
        int par = parent[x], grandPar = parent[par];
        if(par == x) return x;
        parent[x] = grandPar; 
        return find(grandPar);
    }

    public void unite(int a, int b) {
        int rootA = find(a), rootB = find(b);
        if(rootA == rootB) return ;
        int small = rootA, big = rootB;
        if(size[rootA] > size[rootB]){
            small = rootB;
            big = rootA;
        }
        
        // unite two trees;
        parent[small] = big;
        size[big] += size[small];

        if(size[big] > maxSize) maxSize = size[big];
    }
    
}
```

