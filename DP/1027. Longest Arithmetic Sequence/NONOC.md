# Brute Force
Find the difference between two numbers, time O(n^2)
for difference, search same, time O(n^3)
# Thinking
![](%202020-06-15-16-11-27.png)
We could find the difference between two numbers, then we find our task is to let difference add near difference and get as many as same results. 
# DP
I donot know how to write O(n^2) algorithm so i see the answer:

dp[index][diff] equals to the length of arithmetic sequence at index with difference diff.
So dp[index][diff]=any(dp[index_before][diff])+1

Just like brute force, but differences in:

1. Store diff to search in O(1).
2. Just store useful information: Just need longest arithmetic length, so just store necessary index i and difference between two elements before index i.
```
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp={}#(index,difference)
        for i in len(A):
            for j in range(i+1,len(A)):
                dp[j,A[j]-A[i]]=dp.get((i,A[j]-A[i]),1)+1
        return max(dp.values())
```