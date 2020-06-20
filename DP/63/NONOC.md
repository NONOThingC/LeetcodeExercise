This problem is easy.
Time O(nm) space O(nm).
Assume DP[i][j] possible path when robot arrive in i,j.
So 
$$ 
if M[i+1][j+1]=0:
DP[i+1][j+1]=DP[i+1][j]*(M[i+1][j]==0)+DP[i][j+1]*(M[i][j+1]==0);0<=i<m , 0<=j<n
$$

Note: m and n will be at most 100. But data still provide data as [[1]].

```
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if n==0:
            return 0
        if m==1 and n==1:
            return 0 if obstacleGrid[0][0]==1 else 1
        DP=[[0]*n for _ in range(m)]
        DP[0][0]=1
        for i in range(m):
            for j in range(n):
                if(i==0 and j==0):
                    continue
                DP[i][j]=(DP[max(i-1,0)][j]*(obstacleGrid[max(i-1,0)][j]==0)+DP[i][max(j-1,0)]*(obstacleGrid[i][max(j-1,0)]==0))*(obstacleGrid[i][j]==0)
        return DP[m-1][n-1]
```