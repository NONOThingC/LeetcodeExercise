the simple dp method, TLE ,O(nk):

```java
class Solution {
    public int kConcatenationMaxSum(int[] arr, int k) {
        int len = arr.length;
        long[] dp = new long[len];
        long max = -1;
        dp[len - 1] = 0;
        for(;k > 0;k--){
            for(int i = 0;i < len;i++){
                int pos = (i-1 + len) % len;
                if(dp[pos] > 0 ){
                    dp[i] = dp[pos] + arr[i];
                }
                else{
                    dp[i] = arr[i];
                }
                if(dp[i] > max) max = dp[i];
            }
        }
        return max > 0 ? (int)(max % (1000000007)) : 0;
    }
}
```



only three cases have the chance to be the maximum:

	1. the maximum subarray in a single arr.
 	2. the maximum suffix plus the maximum prefix.
 	3. the maximum suffix plus the maximum prefix plus (k-2) *  sum of arr.

time: O(n), space: O(1)

```java
class Solution {
    public int kConcatenationMaxSum(int[] arr, int k) {
        int len = arr.length;
        long sum = 0;
        int s = arr[0];

         // max subarray
        int maxSub = s;
        for(int i = 1;i < len;i++){
            if(s <= 0) s = arr[i];
            else s += arr[i];
            if(s > maxSub) maxSub = s;
        }


        // sum of arr
        for(int i = 0;i < len;i++){
            sum += arr[i];
        }

        // max prefixSum
        int maxPre = -1;
        s = 0;
        for(int i = 0;i < len;i++){
            s += arr[i];
            maxPre = Math.max(s, maxPre);
        }

        // max suffixSum
        s = 0;
        int maxSuf = -1;
        for(int i = len -1;i >= 0;i--){
            s += arr[i];
            maxSuf = Math.max(s, maxSuf);
        }

        long ans = 0;
        if(k == 1) ans = maxSub;
        else{
            ans = Math.max(maxSub, Math.max((k-2)*sum+ maxPre+ maxSuf, maxSuf + maxPre));
        }
        return ans > 0 ? (int)(ans % (1000000007)) : 0;
    }
}
```

