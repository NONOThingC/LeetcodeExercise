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
