以leetcode 416为例：
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t_sum=sum(nums)
        if t_sum%2:
            return False
        t_sum=t_sum//2
        dp=[False for i in range(t_sum+1)]
        dp[0]=True
        for i in range(len(nums)):
            for w in range(t_sum,nums[i]-1,-1):

                dp[w]=dp[w] or dp[w-nums[i]]
                
        return dp[t_sum]
```
总结出模板：
```python

    def onezero_knapsack(nums: List[int]):
        
        dp=[0 for i in range(W+1)]#初始化，注意如果要求刚好的那个值初始化为-float("inf"),可以小于时应该初始化为0,注意要比权重多一个数
        dp[0]=1#取值根据base case确定
        for i in range(len(nums)):#注意只循环前N个数那么多次
            for w in range(W,nums[i]-1,-1):#注意，这里需要倒着更新，而且结束为nums[i]（包含）这个值。
                dp[w]=max(dp[w],dp[w-nums[i]])
        return dp[t_sum]
```