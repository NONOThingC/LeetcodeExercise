**Thinkings** 

dp method, two points needs emphasis: 

1. the transfer equation is essential
2. the initialization condition

We use a two-d array , where s(i)(j) indicates whether the substring that starts from i and ends at j is palindromic.

A string s is palindromic if and only if 

​	a. its substring s(i+1)(j-1)  

​	b. s(i) == s(j)

**Complexity** 

time： O(n^2) space: O(n^2)

```java
class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        boolean[][] dp = new boolean[len][len];
        if(len == 0) return "";
        int maxl = 0, maxr = 0, max = 1;
        // initialization
        for(int i = 0;i < len ;i++) {
            dp[i][i] = true;
            if(i < len - 1) {
                dp[i][i+1] = (s.charAt(i) == s.charAt(i+1));
                if(dp[i][i+1]){
                    max = 2;
                    maxl = i;
                    maxr = i + 1;
                }
            }
        }
        // the transfer eqation: 
        // dp[i][j] = dp[i+1][j-1] & (s[i] == s[j]), if i - j  + 1 > 2
        for(int i = len - 3;i >= 0;i--) {
            for(int j = i + 1;j < len;j++) { 
                if(j - i > 1){
                    dp[i][j] = dp[i+1][j-1] & (s.charAt(i) == s.charAt(j));
                    if(dp[i][j] && j - i + 1 > max) {
                        max = j - i + 1;
                        maxl = i;
                        maxr = j;
                    }
                }
                
            }
        }
        
        return s.substring(maxl, maxr+1);
    }
}
```



---

**Thinkings** 

center expansion

considering that the palindromic string are symmetric, so we can enumerate all the centers and try to expand these center strings to check if they can turn into longer palindromic strings.

**Complexity**

time: O(n^2)  space: O(1)

```java
class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        if(len == 0) return "";
        int max = 1;
        int left = 0, right = 1;
        for(int i = 0;i < len;i++) {
            int len1 = expand(s,i, i);
            int len2 = expand(s,i, i+1);
            int maxLen = Math.max(len1, len2);
            if(maxLen > max) {
                max = maxLen;
                left  = i - (maxLen-1) / 2;
                right = left + maxLen;
            }
        }
        return s.substring(left, right);
    }

    public int expand(String s, int l, int r) {
        int len = s.length();
        while(l >= 0 && r < len && s.charAt(l) == s.charAt(r)){
            l--;
            r++;
        }
        return r - l - 1;
    }
}
```

