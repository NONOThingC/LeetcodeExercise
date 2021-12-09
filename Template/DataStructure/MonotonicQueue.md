```python
q=queue()
for i in range(len(nums)):
    while(q and nums[i]<q[-1]):#维护单调递增队列
        q.pop()
    q.append(i)

```