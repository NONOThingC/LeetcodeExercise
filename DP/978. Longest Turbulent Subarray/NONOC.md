Assume DP[i] is length of a maximum size turbulent subarray of A[0:i](closed interval).

ATTENTION:[] 0,[1],[0,0,0,0],[2,2]
## Iterate by step 1
It is easy to get:
$$
DP[i+1]=DP[i]+1 \\
if(arr[i]>arr[i-1]\quad and \quad arr[i-1]<arr[i-2]\quad or\quad arr[i+1]-arr[i]<arr[i]-arr[i-1])\quad and\quad i>=2 \\
DP[0]=2\\
DP[1]=2
$$
And we could see current state just associate with last state, so it is easy to optimize space complexity to O(1).
But there is a bug because when arr elements are all same, just like arr=[0,0,0,0], we could get 2 but correct answer is 1.

We also need to discuss when len(arr)<2:

1. if len(arr)==1, then answer=1
2. if len(arr)<1, then answer=0
3. if len(arr)==2, then answer=1 when arr[0]==arr[1], answer=2 when arr[0]!=arr[1]

So we know, when len(arr)<=1 just return answer=len(arr)
```python
class Solution:
    def maxTurbulenceSize(self, arr):
        arr_len=len(arr)
        if(arr_len<=1):
            return arr_len
        if(arr_len==2):
            return 2 if arr[0]!=arr[1] else 1
        dp1=2
        dp2=2
        answer=0
        for i in range(2,len(arr)):
            if arr[i]>arr[i-1] and arr[i-1]<arr[i-2]:
                if i%2:
                    dp1+=1
                    dp2=2
                else:
                    dp2+=1
                    dp1=2
            elif arr[i]<arr[i-1] and arr[i-1]>arr[i-2]:
                if i%2:
                    dp2+=1
                    dp1=2
                else:
                    dp1+=1
                    dp2=2
            elif arr[i]==arr[i-1]:
                dp1=1
                dp2=1
            else:
                dp1=2
                dp2=2
            answer=max(answer,dp1,dp2)
        return answer
```
Runtime: 552 ms, faster than 62.90% of Python3 online submissions for Longest Turbulent Subarray.

Memory Usage: 18 MB, less than 20.66% of Python3 online submissions for Longest Turbulent Subarray.

We could see other answer:
```python
def maxTurbulenceSize(self, A):
    best = clen = 0

    for i in range(len(A)):
        if i >= 2 and (A[i-2] > A[i-1] < A[i] or A[i-2] < A[i-1] > A[i]):
            clen += 1
        elif i >= 1 and A[i-1] != A[i]:
            clen = 2
        else:
            clen = 1
        best = max(best, clen)
    return best
```
So when i think of this problem, i have some shortcut:

1. Initial number is not so clear.
2. Not find the mutual exclusion in condition A[i-2] > A[i-1] < A[i] or A[i-2] < A[i-1] > A[i].

Another method is to change A to proper simple information, then scan again.

Runtime: 568 ms, faster than 53.18% of Python3 online submissions for Longest Turbulent Subarray.
Memory Usage: 17.2 MB, less than **100.00%** of Python3 online submissions for Longest Turbulent Subarray.
```python
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i] = 0
            elif A[i] < A[i+1]:
                A[i] = 1
            else:
                A[i] = -1
        A[-1] = -2
        ans = 0
        left = 0
        while left < len(A):
            right = left
            while right + 1 < len(A) and A[right] + A[right+1] == 1:
                right += 1
            ans = max(ans,right-left + 1 + (A[right]>-1))
            left = right + 1
        return ans
```
