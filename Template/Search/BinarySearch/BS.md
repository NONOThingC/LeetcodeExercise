极为优秀的二分法的解释：
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/lan-hong-hua-fen-fa-dan-mo-ban-miao-sha-e7r40/

二分法理解的几个要点就是由于left=mid+{-1,0,+1}造成指针最后位置的变化。+-1最后会造成指针越位，重叠，而+-0指针最后只会相邻。

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

BS的模板的理解：
## 搜索左边边界
```python
def BS(nums,target):
    l,r=0,len(nums)
    while l<r:
        mid=l+(r-l)//2
        if nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            r=mid
        else:
            r=mid#lower bound
    return l
```
在这种情况中，返回的是nums 中**小于** target 的元素有 l 个，注意是小于，也就是说，如果target在数组中有值，就是数组中这个值的最左边那个值；如果target在数组中没有值，就是返回小于它的元素有多少个。这两种情况，换一种说法也可以是刚好大于等于target的第一个数。不过我个人觉得还是记成小于target的元素有l个更好记。


**需要注意的是返回的是小于target的元素有多少个，所以如果目标值*大于*数组中最大值时候，即target>max(nums)时候返回的是len(nums)会到导致越界。**

另一种模板是：
```python
def BS(nums,target):
    l,r=0,len(nums)-1
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            r=mid-1
        else:
            r=mid-1#lower bound
    return l
```
注意这种情况下循环break时候l比r大1.而返回l的逻辑和上面那个模板完全一致。
一模一样的逻辑，不要听labuladong乱写。边界条件和上面完全一样。

举个例子来说，

`[1,1,3,3,4,7,7,9]`
如果搜索0，那么返回的是0.
如果搜索存在的值3，那么返回的是2,nums[l]刚好取到最左边那个3；
如果搜索不存在的值2，那么返回的也是2，nums[l]刚好取到3.
如果搜索9，那么返回的是7，nums[l]刚好取到9.
如果搜索10，那么返回是8，会越界注意需不需要判断。

**所以这种情况就需要在返回时候做一个判断来看nums[l]==target以达到来看是不是自己想要的输出。**
## 搜索右侧边界
```python
def BS(nums,target):
    l,r=0,len(nums)
    while l<r:
        mid=l+(r-l)//2
        if nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            r=mid
        else:
            l=mid+1
    return l
```

另一种模板是：
```python
def BS(nums,target):
    l,r=0,len(nums)-1
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            r=mid-1
        else:
            l=mid+1
    return l
```
注意这种情况下循环break时候l比r大1.而返回l的逻辑和上面那个模板完全一致。
一模一样的逻辑，不要听labuladong乱写。边界条件和上面完全一样。

在这种情况中，返回的是nums 中**大于等于** target 的元素有 l 个，注意是大于等于，跟搜素左边边界刚好互补。也就是说，如果target在数组中有值，就是数组中这个值的最右边那个值+1，也就是开区间，可以看下面的例子；如果target在数组中没有值，就是返回大于等于它的元素有多少个。这两种情况，换一种说法也可以是刚好大于target的第一个数。不过我个人觉得还是记成大于等于target的元素有l个更好记。

**需要注意的是返回的是大于等于target的元素有多少个，所以如果目标值*大于等于*数组中最大值时候，即target>=max(nums)时候返回的是len(nums)会到导致越界。**

举个例子来说，

`[1,1,3,3,4,7,7,9]`
如果搜索0，那么返回的是0.
如果搜索存在的值3，那么返回的是4,nums[l]取到4；
如果搜索不存在的值2，那么返回的也是2，nums[l]刚好取到3.
如果搜索9，那么返回的是8，nums[l]会越界.
如果搜索10，那么返回是8，会越界注意需不需要判断。

**所以这种情况就需要在返回时候做一个判断来看nums[l]==target以达到来看是不是自己想要的输出。**

## 搜索某个数字
```python
def BS(nums,target):
    l,r=0,len(nums)
    while l<r:
        mid=l+(r-l)//2
        if nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            r=mid
        else:
            return target
    return -1#或者
    return l
```
注意这种情况下，如果是`return l`，搜索不到会返回小于target的数目，如果搜索到了，返回的是=target的任意一个，无法保证左右。注意l==r是没有进行判断的，如果单独进行判断就可以改对了。
所以这种情况一般建议用下面这个模板：
```python
def BS(nums,target):
    l,r=0,len(nums)-1
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            r=mid-1
        else:
            return target
    return -1
    return l
```
注意这种情况下，如果是`return l`，搜索不到会返回小于target的数目，如果搜索到了，返回的是=target的任意一个，无法保证左右。


## 搜索某个check函数

以上搜左右边界模板有个问题，其表达意义是小于和大于等于，如果是满足check函数的情况，大于等于就会造成问题。

因为大于等于的话实际对于等于的值会一直往右边走直到超过界限，而如果target在数组不存在，又会选到刚好大于的那个答案。


 [check为假][check为真]
l                    r

这种情况下可以考虑以下模板：
这个模板最后会停在刚好的边界上，l在假的边界上，r在真的边界上。 

主要是为了求得使check为真的边界条件。
```python
def BS(check,target):
    l,r=-1,len(nums)#l需要可选值之前一个值,r是取不到的那个值    
    while l+1<r:
        mid=l+(r-l)//2
        if check(mid):
            r=mid#可能跟l相反
        else:
            l=mid
    
    # if check(l): 
    #     choose l
    # else:
    #     choose r
    return l
```

#### 细节1：l为什么初始化为-1，r初始值为N？
主要是为了handle check为全真或者全假的情况。

#### 细节2：mid是否始终处于[0,N)以内？
首先看最小值，根据`l+1<r`，l_min=-1,r_min=1,此时m_min=0;
再看最大值，l_max=N-2,r_max=N,此时m_min=N-1;

#### 细节3：更新指针能不能写成l=m+1或者r=m-1？
这种写法容易出错，因为l和m并会越出界。

#### 细节4：程序会不会死循环？
不会




 [check为假][check为真]
           lr

至于注释那个部分，指的是l一开始就不能取到那个范围的时候。

如果是

`[check为真][check为假]`

的形式,注意l和r要反过来。

思考过程如下：

```
例如 mid=[0,1,2,3,4,5,6,...]
   check=[0,0,0,1,1,1,1,...]
```

如果我要取到check为1的分界点，那么很明显check为false的时候需要控制l=mid
否则r=mid.

```
例如 mid=[0,1,2,3,4,5,6,...]
   check=[1,1,1,0,0,0,0,...]
```
如果我要取到check为1的分界点，那么很明显check为True的时候需要控制l=mid
否则r=mid.


#### 例子选讲

![](%202022-04-04-13-30-10.png)

1.
```python
nums=[1,2,3,5,5,5,8,9]
def bs_search(nums):
    l,r=-1,len(nums)
    while l+1<r:
        mid=l+(r-l)//2
        if nums[mid]>=5:
            r=mid
        else:
            l=mid
    return r
a=bs_search(nums)
```

2.
```python
nums=[1,2,3,5,5,5,8,9]
def bs_search(nums):
    l,r=-1,len(nums)
    while l+1<r:
        mid=l+(r-l)//2
        if nums[mid]>=5:
            r=mid
        else:
            l=mid
    return l
a=bs_search(nums)
```

3.
```python
nums=[1,2,3,5,5,5,8,9]
def bs_search(nums):
    l,r=-1,len(nums)
    while l+1<r:
        mid=l+(r-l)//2
        if nums[mid]>5:
            r=mid
        else:
            l=mid
    return r
a=bs_search(nums)
```

4.
```python
nums=[1,2,3,5,5,5,8,9]
def bs_search(nums):
    l,r=-1,len(nums)
    while l+1<r:
        mid=l+(r-l)//2
        if nums[mid]<=5:
            l=mid
        else:
            r=mid
    return l
a=bs_search(nums)
```

5. 寻找大于等于9的第一个元素
```python
nums=[1,2,3,5,5,5,8,9]
def bs_search(nums):
    l,r=-1,len(nums)
    while l+1<r:
        mid=l+(r-l)//2
        if nums[mid]>=9:
            r=mid
        else:
            l=mid
    return r
a=bs_search(nums)
```

6.寻找大于9的第一个元素
```python
nums=[1,2,3,5,5,5,8,9]
def bs_search(nums):
    l,r=-1,len(nums)
    while l+1<r:
        mid=l+(r-l)//2
        if nums[mid]>9:
            r=mid
        else:
            l=mid
    return r
a=bs_search(nums)
```