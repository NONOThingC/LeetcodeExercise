# 清晰的介绍：https://segmentfault.com/a/1190000004410119

def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
 
def partition(array,l,r):
    #双指针法,详见上面链接
    p=array[l]
    while l<r:
        while l<r and array[r]>=p:#等于的时候一直减，于是返回最左边的
            r-=1
        array[l]=array[r]
        while l<r and array[l]<p:
            l+=1
        array[r]=array[l]
    array[l]=p#容易忘记
    return l#此时l==r
        
def partition(array, l, r):#左右都是闭区间，但是用r来自作为分割元素
    x = array[r]
    pivot = l# 表示分界点的位置
    for ind in range(l, r):
        if array[ind] < x:#注意无等号的时候返回的是相等值的最左边那个数，比如9444返回的是0，4444返回的是0；而有等号的时候返回的是相等的最右边那个，比如9444返回的是2，4444返回的是3
            array[pivot], array[ind] = array[ind], array[pivot]
            pivot += 1
    array[pivot], array[r] = array[r], array[pivot+1]#做完后pivot左边和包含pivot都比x小于等于，pivot右边都比x大于，于是把pivot+1即可。
    return pivot

def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])
