# Matrix Block Sum
Use basic search, time O(n^2*m^2),space O(1):

```
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

Use prefix sum:

```java
class Solution {
    public int[][] matrixBlockSum(int[][] mat, int K) {
        int h = mat.length, w = mat[0].length;
        // 为了不用考虑边界，设置prefixSum为 h+1 * w+1。
        // 对应的位置关系为 prefixSum[i][j] 记录 mat[0][0] -> mat[i-1][j-1]的和
        int[][] prefixSum = new int[h+1][w+1];
        
        int[][] ans = new int[h][w];

        for(int i = 1;i <= h;i++){
            for(int j = 1;j <= w;j++){
                prefixSum[i][j] = prefixSum[i][j-1] + prefixSum[i-1][j] 
                                    - prefixSum[i-1][j-1]+ mat[i-1][j-1];
            }
        }

        for(int i = 0;i <  h;i++){
            for(int j = 0;j < w;j++){
            	/* 可以推出 ans[i][j]与前缀和关系:
            	* ans[i][j] = prefixSum[i+1+k][j+1+k] + prefixSum[i+1-k][j+1-k]
            	*             - prefixSum[i+1-k][j+1+k] - prefixSum[i+1+k][j+1-k]
            	* 具体需要根据边界做调整。
            	*/
                int x1 =Math.min(j+1+K,w), y1=Math.min(i+1+K,h);
                int x2 =Math.min(j+1+K,w), y2=Math.max(i-K,0);
                int x3 =Math.max(j-K,0), y3=Math.min(i+1+K,h);
                int x4 =Math.max(j-K,0), y4=Math.max(i-K,0);

                ans[i][j] = prefixSum[y1][x1] + prefixSum[y4][x4] 
                            - prefixSum[y2][x2] - prefixSum[y3][x3];
            }
        }

        return ans;
    }
}
```

both space and time : O(mn)