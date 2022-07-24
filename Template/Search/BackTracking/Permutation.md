# 排列组合子集中的库函数
如果不是单独写，就用库函数就行。
https://zhuanlan.zhihu.com/p/370972191
优质教程：https://segmentfault.com/a/1190000040142137
```python
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    n = len(iterable)
    if r > n: #r大于数组的长度没有意义
        return

    indices = list(range(n)) # indices存放数组的index为0~9

    cycles = list(range(n, n-r, -1))# 初始cycles=[10,9,8],cycles的长度就是r
# 这里可以看到，相对于combinations，permutations多了cycles这一项

    yield [iterable[i] for i in indices[0:r]] # 同样，假设iterable即数组nums
# 为 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，r=3，初始返回 [1,2,3]

    while True:
        for i in reversed(range(r)):# 同样，每次执行reversed(range(r))
# 当r=3的时候，每次遍历的数组index 都是[2,1,0]
# 初始cycles=[10,9,8]
            cycles[i] -= 1 #因为前面使用list(range(n, n-r, -1))生成cycles，所以
# cycles实际上每一个位置的index都是多1的，比如[10,9,8]其实对应的是原始数组[9,8,7]的index的位置
# 经过了cycles[i] -= 1 cycles=[10,9,7]
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
# j=7,i=2
                indices[i], indices[-j] = indices[-j], indices[i]
# 等价于 indices[i], indices[n-j] = indices[n-j], indices[i]
# 实际是交换了 iterable[2]和iterable[3]的位置
# indices变成了 [0, 1, 3, 2, 4, 5, 6, 7, 8, 9]
                yield [iterable[i] for i in indices[0:r]]
                break
        else:
            return
```

```python
def combinations(iterable, r): ## 这个也太方便了
    n = len(iterable) # iterable 就是你要做组合的数组或者其它可迭代对象，一般leetcode
#里都是以数组形式存在

    if r > n:# 如果你要进行排列的数量超过数组长度显然没有意义啊，比如[1,2,3,4] ，排列数量为5阶，无意义，
# 直接返回空
        return

    indices = list(range(r)) #indices，核心，每一次得到的组合的数组索引index
# 下面以 [1,2,3,4,5,5]为例，假设r=3，即做3阶组合

    yield [iterable[i] for i in indices] 
    ####### 返回第一个组合的index[0,1,2]对应的value为 [1,2,3]
    
    ## 这里就使用yield其实类似于直接顺序执行
## yield 和return功能形式相似，只不过是一个一个流式输出的；
## 这里的整段代码也好理解，可以这么理解，把yield看作print，整段代码的yield处就类似于做print，一个一个输出
# 只不过yield可以生成一个迭代器按照书顺序输出具体的值，这些值可以进行进一步的操作而已
# 这里的整段代码的实际运行顺序是顺序输出的


   while True:

        for i in reversed(range(r)):

            if indices[i] != i + n - r:
                break
        else:
            return
        ## 这里的for 。。。。到else：return 的功能是用于判断是否达到终止，比如上面的例子
# [1,2,3,4,5,5]，r=3时，最终终止的那个组合的index是 [3,4,5],对应的原数组的值为[4,5,5]，注意，
#通过index进行判断而不是index对应的值来进行判断
        
        # 为了更好理解，下面完整的举个例子:
# 初始[0,1,2]的index，combinations的实现默认从最后一个位置开始改变，因为上面的for循环
# 使用 reversed从indices的最后一个数开始判断
# 此时返回的i=2

        indices[i] += 1
        # [0,1,2]—> [0,1,3]
        for j in range(i+1, r): # 此时这部分为for j in range(3,3)不执行
            indices[j] = indices[j-1] + 1
            
        yield [iterable[i] for i in indices]
```

## 排列篇

参考文章：https://segmentfault.com/a/1190000040142137###

To handle duplication, just avoid inserting a number after any of its 
duplicates.

#### 插入法：思想是把数字一个一个插入到各个位置上，但如果要插的数字和已有数字重复了，那就不用再插了。
```python
def permuteUnique( nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for each_ans in ans:#each_ans 是每个答案
            for i in range(len(each_ans)+1):# insert n to every sequence
                new_ans.append(each_ans[:i]+[n]+each_ans[i:])
                if i<len(each_ans) and each_ans[i]==n: break              #handles duplication
        ans = new_ans
    return ans
```
Below is a backtracking solution:
```python
from collections import Counter
def permuteUnique(self, nums):
    def btrack(path, counter):
        if len(path)==len(nums):
            ans.append(path[:])
        for x in counter:  # dont pick duplicates
            if counter[x] > 0:
                path.append(x)
                counter[x] -= 1
                btrack(path, counter)
                path.pop()
                counter[x] += 1
    ans = []
    btrack([], Counter(nums))
    return ans
```

#### 定首位元素后的交换

Recall Permutation I, where there is no duplicate.
The basic idea was to enumerate all possibilities of the first element, and recursively permute the remaining, then concatenate.

For example: 123
let 1 be the first element, recursively permute 23
let 2 be the first element, recursively permute 13
let 3 be the first element, recursively permute 12

I'll show two versions here; a more intutive recursion and less intutive (I think) backtracking

#### intuitive recursion
```
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return [[]]
        res = []
        for i in range(n):
            for p in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + p)
        return res
```
#### backtracking 
```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        def dfs(l):
            if l == n-1:
                res.append(list(nums))
                return 
            for i in range(l, n):
                nums[l], nums[i] = nums[i], nums[l]   # swap nums[l] and nums[i]
                dfs(l+1)
                nums[l], nums[i] = nums[i], nums[l]  # swap them back
        dfs(0)
        return res
```
Now consider the case where there are duplicates in nums.
The idea is still the same. except we only put the duplicated element in the front once.

For example, 11223
let 1 be the first element, recursively permute 1223
let 2 be the first element, recursively permute 1123
let 3 be the first element, recursively permute 1122

#### How to adapt the previous code to take care of duplicates?
We can simply pick out the unique element, and recursively permute the remainining.

#### intuitive recursion (beat 60.77%) 
```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        res = []
        for i in set(nums):
            remaining = list(nums)
            remaining.remove(i)
            for p in self.permuteUnique(remaining):
                res.append([i] + p)
        return res
```
#### backtracking  (beat 94.13%) 
```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        def dfs(nums, l):
            if l == n-1:
                res.append(list(nums))
                return 
            for i in set(nums[l:]):
                remaining = nums[l:]
                remaining.remove(i)
                dfs(nums[:l] + [i] + remaining, l+1)
        dfs(nums, 0)
        return res
```

一个跟子集问题类似的模板：
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]
        
        self.backtrack([], nums, check)
        return self.res
        
    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol+[nums[i]], nums, check)
            check[i] = 0
```

在上面改动了下让它更好背
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [0 for i in range(len(nums))]
        sol=[]
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):

                if used[i] == 1 or (i > 0 and nums[i] == nums[i-1] and used[i-1] == 0):
                    continue
                used[i] = 1
                sol.append(nums[i])
                backtrack()
                sol.pop()
                used[i] = 0
        
        
        
        backtrack()
        return res
```

## 子集篇

```java
class Solution {
    List<Integer> t = new ArrayList<Integer>();
    List<List<Integer>> ans = new ArrayList<List<Integer>>();

    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        for (int mask = 0; mask < (1 << n); ++mask) {
            t.clear();
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) != 0) {
                    t.add(nums[i]);
                }
            }
            ans.add(new ArrayList<Integer>(t));
        }
        return ans;
    }
}
```
相对应的python代码：


也可以考虑回溯法
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []  #存放符合条件结果的集合
        path = []  #用来存放符合条件结果
        def backtrack(nums,startIndex):
            res.append(path[:])
            for i in range(startIndex,len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:  #我们要对同一树层使用过的元素进行跳过，如果不需要跳过重复元素，就可以直接不要这里
                    continue
                path.append(nums[i])
                backtrack(nums,i+1)  #递归
                path.pop()  #回溯
        nums = sorted(nums)  #去重需要排序
        backtrack(nums,0)
        return res
```

更好背的版本：
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        path=[]
        ans=[]
        def rec(s):
            ans.append(path[:])
            for i in range(s,len(nums)):
                if i>s and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                rec(i+1)
                path.pop()
        nums.sort()
        rec(0)
        return ans
```
## 组合篇
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        path=[]
        def rec(s,l):
            if l==k:
                ans.append(path[:])
                return
            for i in range(s,n+1):
                path.append(i)
                rec(i+1,l+1)
                path.pop()
        rec(1,0)
        return ans
```

组合总和2，要求不重复：leetcode40:  https://leetcode-cn.com/problems/combination-sum-ii/
```python
class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(s, path, target):
            if target == 0:
                res.append(path[:])
                return

            for i in range(s, size):
                if candidates[i] > target:
                    break

                if i > s and candidates[i - 1] == candidates[i]:
                    continue

                path.append(candidates[i])
                dfs(i + 1, path, target - candidates[i])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res
```

