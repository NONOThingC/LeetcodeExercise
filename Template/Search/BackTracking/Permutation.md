To handle duplication, just avoid inserting a number after any of its duplicates.

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