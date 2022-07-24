Here I sort (index, value) pairs. The value is used for the sorting and the index is used for tracking the jumps.

```python
leetcode 315
def countSmaller(self, nums):
    def sort(enum):
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller
```
Template: sort only the indexes. 

```python
def MergeSort( nums):
    def sort(indexes):
        half = len(indexes) / 2
        if half:
            left, right = sort(indexes[:half]), sort(indexes[half:])
            for i in range(len(indexes))[::-1]:
                if not right or left and nums[left[-1]] > nums[right[-1]]:
                    indexes[i] = left.pop()
                else:
                    indexes[i] = right.pop()
        return indexes
    return sort(range(len(nums)))
```
Old version

```java
class Merge {

    // 用于辅助合并有序数组
    private static int[] temp;

    public static void sort(int[] nums) {
        // 先给辅助数组开辟内存空间
        temp = new int[nums.length];
        // 排序整个数组（原地修改）
        sort(nums, 0, nums.length - 1);
    }

    // 定义：将子数组 nums[lo..hi] 进行排序
    private static void sort(int[] nums, int lo, int hi) {
        if (lo == hi) {
            // 单个元素不用排序
            return;
        }
        // 这样写是为了防止溢出，效果等同于 (hi + lo) / 2
        int mid = lo + (hi - lo) / 2;
        // 先对左半部分数组 nums[lo..mid] 排序
        sort(nums, lo, mid);
        // 再对右半部分数组 nums[mid+1..hi] 排序
        sort(nums, mid + 1, hi);
        // 将两部分有序数组合并成一个有序数组
        merge(nums, lo, mid, hi);
    }

    // 将 nums[lo..mid] 和 nums[mid+1..hi] 这两个有序数组合并成一个有序数组
    private static void merge(int[] nums, int lo, int mid, int hi) {
        // 先把 nums[lo..hi] 复制到辅助数组中
        // 以便合并后的结果能够直接存入 nums
        for (int i = lo; i <= hi; i++) {
            temp[i] = nums[i];
        }

        // 数组双指针技巧，合并两个有序数组
        int i = lo, j = mid + 1;
        for (int p = lo; p <= hi; p++) {
            if (i == mid + 1) {
                // 左半边数组已全部被合并
                nums[p] = temp[j++];
            } else if (j == hi + 1) {
                // 右半边数组已全部被合并
                nums[p] = temp[i++];
            } else if (temp[i] > temp[j]) {
                nums[p] = temp[j++];
            } else {
                nums[p] = temp[i++];
            }
        }
    }
}
```


## 计数排序

```python
citations=[2,1,5,7,2,3,1,6,0]
score2cnt=[0]*(max(citations)+1)
for citation in citations:
    score2cnt[citation]+=1
s2cum_cnt=[0]*(max(citations)+1)
s2cum_cnt[0]=score2cnt[0]
for i in range(1,len(score2cnt)):
    s2cum_cnt[i]=s2cum_cnt[i-1]+score2cnt[i]

# 建立好累积次数的映射关系后，就可以将倒着来看该把哪个元素放哪里
ans=[0]*len(citations)
for i in range(len(citations)-1,-1,-1):
    ele=citations[i]
    s2cum_cnt[ele]-=1# 减1建立与index的映射
    ans[s2cum_cnt[ele]]=citations[i]#因为累积有多少个就代表需要把这个元素放在哪里
```