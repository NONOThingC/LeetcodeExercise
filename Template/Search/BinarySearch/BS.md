1. Pay attention to the opening and closing of the interval.

```python
def BinarySearch(nums,target):
    left=0
    right=...#区间开闭决定
    while(...):#区间开闭决定
        mid=left+(right-left)//2
        if nums[mid]==target:
            pass#搜索方式决定，如果要搜最左那应该让右边收缩
        if nums[mid]<target:
            left=...#区间开闭决定
        if nums[mid]>target:
            right
    return ... #检查索引越界情况

```

```C++
int BinarySearch(int[] nums,int target)
{
    int left=0,right=...;
    while(...)
    {
        int mid=left+(right-left)/2;
        if (nums[mid]==target)
            {
                ...
            }
        else if (nums[mid]<target)
        {
            left=...
        }
        else if (nums[mid]>target)
        {
            right=...
        }
    }
    return ...;
}
```