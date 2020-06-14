classic problem.
# Pre-process
because odd+even=even, so we add * to our string gap\head\tail.

# DP
1. Assuming dp[i][j] is from i to j, if string i:j is Palindromic Substring. Then we get:

![](%202020-06-12-14-05-07.png)

This algorithm time cost O(n^2), space cost O(n^2).

2. Assuming dp[i] is palindromic radius of the centre of string i. So for every element, just search its longgest radius.

This algorithm time cost O(n^2), space cost O(1).

# Manacher's Algorithm
Runtime: 120 ms, faster than 95.19% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.9 MB, less than 45.68% of Python3 online submissions for Longest Palindromic Substring.
Time O(n), space O(n)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pre_process(s):
            return "-"+"-".join(list(s))+"-"

        pre_s=pre_process(s)
        len_ps=len(pre_s)
        P=[0]*len_ps
        centre=0
        r=0# radius
        max_r=0
        max_i=-1
        for i,se in enumerate(pre_s):
            if(centre+r>i):
                P[i]=min(centre+r-i,P[2*centre-i])
            j=i+P[i]+1
            k=i-P[i]-1
            while(j<len_ps and k>-1 and pre_s[j]==pre_s[k]):
                P[i]+=1
                j+=1
                k-=1
            if(i+P[i]>r+centre):
                centre=i
                r=P[i]
            if(max_r<r):
                max_r=r
                max_i=i
        a_str="".join(pre_s[max_i-max_r:max_i+max_r].split('-'))
        return a_str
```