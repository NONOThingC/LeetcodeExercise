Wrong because I did not get hang of description.
Because of 1027, we could use same method to get answer with time O(n^2) space O(n).
So a better method is less than O(n^2).
1. So we consider hashmap to function it. This question is similar to question 128, hashmap search neighbor, union find is useful for this question, we just need to turn 1 to k.
```python
class Solution:
    def longestSubsequence(self, arr, difference):
        arr_len=len(arr)
        import collections
        arr_dict=collections.defaultdict(int)
        ans=0
        for num in arr:
            if(arr_dict[num]!=0):
                continue
            arr_dict[num]=arr_dict[num+difference*arr_dict[num+difference]]=arr_dict[num-difference*arr_dict[num-difference]]=arr_dict[num+difference*arr_dict[num+difference]]+arr_dict[num-difference*arr_dict[num-difference]]+1
            ans=max(ans,arr_dict[num])
        return ans
```
2. And union find is also a good way. Just as 128.
```python
class UnionFind():
    def __init__(self,N):
        self.par=list(range(N))
        self.rank=[1]*N

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
        x=self.find_root(x)
        y=self.find_root(y)
        if(x==y):
            return

        if(self.rank[x]<=self.rank[y]):
            self.par[x]=y
            self.rank[y]+=self.rank[x]
        else:
            self.par[y]=x
            self.rank[x]+=self.rank[y]

    def max_rank(self):
        return max(self.rank) if(len(self.rank)) else 0


    def same(self,x,y):
        """
        verify if x,y is in same set.
        """
        return self.find_root(x)==self.find_root(y)
import collections
arr_set=set(arr)
arr2in=collections.defaultdict(int)
for i,ele in enumerate(arr_set):
    arr2in[ele]=i
UF=UnionFind(len(arr_set))
for i,element in enumerate(arr2in.keys()):
    if(element+difference in arr2in):
        UF.unite(arr2in[element],arr2in[element+difference])
    if(element-difference in arr2in):
        UF.unite(arr2in[element],arr2in[element-difference])
return UF.max_rank()
```
