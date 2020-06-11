Because algorithm should run in O(n) complexity.

1. so one idea is that when we iterable through the array, we should put it in a proper position and then search neighbor. But when a new value comes in, we should update all the neighbors, which time cost O(n^2),space O(n).
But when i see discussion in [leetcode](https://leetcode.com/problems/longest-consecutive-sequence/discuss/41088/Possibly-shortest-cpp-solution-only-6-lines), i find, in fact, we just need to update head neighbors and tail neighbors, which time cost O(n),space O(n).
This answer is so ingenious!
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        import collections
        nums_dict=collections.defaultdict(int)
        r=0
        for num in nums:
            if(nums_dict[num]!=0):
                continue
            nums_dict[num]=nums_dict[num+nums_dict[num+1]]=nums_dict[num-nums_dict[num-1]]=nums_dict[num-1]+nums_dict[num+1]+1
            r=max(r,nums_dict[num])
        return r
```


2. This idea is from leetcode offical answer, it iterates through nums and finds if num-1,num+1 is in the nums_set.time cost O(n),space O(n)
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        max_len=0
        for num in nums_set:
            if(num-1 not in nums_set):
                iter_num=num
                iter_len=1
                while(iter_num+1 in nums_set):
                    iter_num+=1
                    iter_len+=1
                max_len=max(max_len,iter_len)
        return max_len
```
3. Also, union find is useful for this question.
> Runtime: 68 ms, faster than 35.27% of Python3 online submissions for Longest Consecutive Sequence.
> Memory Usage: 15.4 MB, less than 14.95% of Python3 online submissions for Longest Consecutive Sequence.

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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


        nums_map={}
        UF=UnionFind(len(nums))
        for i,num in enumerate(nums):
            if num in nums_map:
                continue
            nums_map[num]=i
            if num+1 in nums_map:
                UF.unite(i,nums_map[num+1])
            if num-1 in nums_map:
                UF.unite(i,nums_map[num-1])
        return UF.max_rank()

```