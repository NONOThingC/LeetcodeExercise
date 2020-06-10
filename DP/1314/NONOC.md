# Matrix Block Sum
Use basic search, time O(n^2*m^2),space O(1):

```python
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        a=[]
        weight=len(mat)
        height=len(mat[0])
        for i in range(weight):
            templist=[]
            for j in range(height):
                ans=0
                for m in range(max(i-K,0),min(i+K+1,weight)):
                    for n in range(max(j-K,0),min(j+K+1,height)):
                        ans+=mat[m][n]
                templist.append(ans)
            a.append(templist)
        return a
```

Use prefix sum, time O(mn) space o(mn):

```python
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        psum=[[0]*n for _ in range(m)]
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            s=0
            for j in range(n):
                s+=mat[i][j]
                if(i>0):
                    psum[i][j]=s+psum[i-1][j]
                else:
                    psum[i][j]=s
        for i in range(m):
            for j in range(n):
                r1_low=i-K
                r2_low=j-K
                r1_high=min(i+K,m-1)
                r2_high=min(j+K,n-1)
                dp[i][j]=psum[r1_high][r2_high]
                if(r1_low>0):
                    dp[i][j]-=psum[r1_low-1][r2_high]
                if(r2_low>0):
                    dp[i][j]-=psum[r1_high][r2_low-1]
                if(r1_low>0 and r2_low>0):
                    dp[i][j]+=psum[r1_low-1][r2_low-1]
        return dp
```

踩坑的地方是，没有注意到做减法时候r1_low、r2_low应该-1，其实可以更改r1_low,r2_low来解决。