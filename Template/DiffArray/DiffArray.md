```python
class DiffArray()
    def __init__(self,nums) -> None:
        # The first step is to use a same length array to record difference between two array.
        self.diff=[nums[0]]
        self.n=len(nums)
        for i in range(1,n):
            self.diff.append(nums[i]-nums[i-1])
        
    def get_res(self):
        # For difference array(DA), to get initial array, use the last element add current element in DA
        res=[self.diff[0]]
        for i in range(1,n):
            res.append(res[-1]+self.diff[i])
        return res

    def increment(self,start,end,val):
        # [start,end]
        self.diff[start]+=val
        # Because get_res, so just add start element and minus end+1 element.
        if end+1<self.n:
            self.diff[end+1]-=val
```