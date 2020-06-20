This problem is easy.

Assume DP[i][j] possible path when robot arrive in i,j.
So $$ DP[i+1][j+1]=DP[i+1][j]+DP[i][j+1];0<=i<m , 0<=j<n $$
But for this problem, it is very easy because just as image below:
![](%202020-06-20-18-59-18.png)
We just need to use combine number $C_{m+n-2}^{m-1}$ to output the result.
```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from scipy.special import comb
        return int(comb(m+n-2,m-1))
```