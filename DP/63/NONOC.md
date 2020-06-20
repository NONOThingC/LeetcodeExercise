This problem is easy.

Assume DP[i][j] possible path when robot arrive in i,j.
So 
$$ 
if M[i+1][j+1]=0:
DP[i+1][j+1]=DP[i+1][j]*(M[i+1][j]==0)+DP[i][j+1]*(M[i][j+1]==0);0<=i<m , 0<=j<n
$$
