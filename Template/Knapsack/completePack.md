以leetcode 518为例总结出模板：
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0 for i in range(amount+1)]
        dp[0]=1
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j]=dp[j]+dp[j-coins[i]]
        return dp[amount]
```
跟01背包不同的地方就是内循环的更新方向，一个比较合理的解释是完全背包问题需要过往多个值，所以要正向更新。
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #需要注意的地方和01背包模板相同
        dp=[0 for i in range(amount+1)]
        dp[0]=1
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):#注意是正向更新
                dp[j]=dp[j]+dp[j-coins[i]]
        return dp[amount]
```
