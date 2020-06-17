arr = [1,5,7,8,5,3,4,2,1], difference = -2
Because of 1027, we could use same method to get answer with time O(n^2) space O(n).

So a better method is less than O(n^2).

It is obvious best time complexity is O(n).

let dp[j] is longest arithmetic subsequence at tail j.
dp[j]= dp[j-difference]+1 

Runtime: 536 ms, faster than 99.57% of Python3 online submissions for Longest Arithmetic Subsequence of Given Difference.
Memory Usage: 27.3 MB, less than 14.89% of Python3 online submissions for Longest Arithmetic Subsequence of Given Difference.

Easy!
```python
class Solution:
    def longestSubsequence(self, arr, difference):
        import collections
        dp=collections.defaultdict(int)
        for i in arr:
            dp[i]=dp[i-difference]+1
        return max(dp.values())
```
