Sub-problem is Maximum continuous subsequence. If just concat K list, time cost $O(k*len(arr))$.
But if we observe follow figure, we can see that:
![](%202020-06-10-13-21-51.png)
Because K>0, so the head sequence and tail sequence may be concated.

1. For every sequence, calculate prefix sum, if psum[-1]<=0, then just decide a sequence, because when concat two list, the former one pays no effect to the latter.
2. if now psum!=0 is in every element, answer=max(prefix[-1]+(k-2)*sum(arr)+max(prefix_sum_include_negative),max_before). because in the secord sequence, if result of the secord prefix sum with initial sum equals to psum[-1], then the middle of K-2 array would be calculated in our results, and the last sequence would just add the max value of prefix sum(including negative).

![](%202020-06-10-14-54-00.png)
3. if psum==0 in middle element, then answer=max(prefix_sum_after,max_before)
```python
class Solution:

    def kConcatenationMaxSum(self,arr, k):
        psum=0
        psum1=0
        max_include_negative=-10**5
        max_before=0
        for i in arr:
            psum+=i
            psum1+=i
            max_include_negative=psum1 if (psum1>max_include_negative) else max_include_negative
            psum=max(0,psum)
            max_before=psum if (psum>max_before) else max_before
        if(k==1 or psum<1):
            return max_before%(10**9 + 7)
        else:
            record_sum=psum
            record_max=max_include_negative
            psum=psum # Increase readability
            for i in arr:
                psum+=i
                psum=max(0,psum)
                max_before=psum if (psum>max_before) else max_before
                if(psum==0):
                    return max_before%(10**9 + 7)    
        
        return max(max_before,record_sum+(k-2)*sum(arr)+record_max)%(10**9 + 7)

```

And there is another solution, cause two sequence need to identify, then just add sum(arr)*(k-2):
```python
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = int(10e8+7)
        if k == 1 : return self.kadane(arr)%mod
        
        sum_ = sum(arr)
        arr = arr+arr
        if sum_ >= 0 :
            return (self.kadane(arr) + sum_*(k-2))%mod
        else :
            return self.kadane(arr)%mod
    
    def kadane(self, arr) :
        curr = 0
        max_ = float('-inf')
        
        for num in arr :
            curr += num
            if curr < 0 : curr = 0
            if curr > max_ : max_ = curr
        
        return max_
```