1. Similar to 1027,let dp[tail] means Longest Increasing Subsequence length at end element tail.
Time O(n^2), space O(n).
dp[tail]=max(dp[tail_before<tail])+1
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_nums=len(nums)
        if(len_nums==0):
            return 0
        dp=[0]*len_nums
        for tail in range(len_nums):
            max_value=0
            for i in range(0,tail):
                if nums[tail]>nums[i]:
                    max_value=max(max_value,dp[i])
            dp[tail]=max_value+1
        return max(dp)
```

2. Binary search and replace.
Time O(nlogn), space O(n).
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            j=bisect.bisect_left(ans,i)
            if(j==len(ans)):
                ans.append(i)
            else:
                ans[j]=i
        return len(ans)
```