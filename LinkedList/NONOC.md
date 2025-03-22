# 链表的初始值
可以用一个`dummy=LinkedList()`表达初值，
最后返回`dummy.next`即可。

# 链表题解法思路
双指针，快慢指针，考虑把链表相连或者接成环状。

# 链表交换题的思路
交换题只有下面三个要点：
1. 一般来说，交换链表的题需要三个指针，领先于所交换范围的h,处于交换前一位置的pre，处于交换位置的cur，交换范围之后的tmp。只交换一次的只需要两个指针。

2. 如果用了上述三个指针，那么循环判断条件该是：
```python
while cur and cur.next:
```
如果是只要两个指针的，通常一个判断条件即可。
```python
while cur.next:
```

3. 头指针前添加一个dummy，以防止涉及第一个节点的交换出错。
```python
dummy=ListNode()
dummy.next=head
h=dummy
pre=dummy
cur=dummy.next
```
# 链表合并题
1. 合并两个链表：
```python
dummy=ListNode()
cur=dummy#注意是这个而不是dummy.next，否则下面的cur=l1会导致失效
while l1 and l2:
    if l1.val<l2.val:
        cur.next=l1
        l1=l1.next
        cur=cur.next
    else:
        cur.next=l2
        l2=l2.next
        cur=cur.next
if l1 or l2:
    cur.next=l1 or l2
return dummy.next
```

2. 合并K个链表：
```python
# mergesort那种原理
def merge2Lists(a,b):
    dummy=ListNode()
    current=dummy
    while a and b:
        if a.val<b.val:
            current.next=a
            a=a.next
        else:
            current.next=b
            b=b.next
        current=current.next
    if a:
        current.next=a
    if b:
        current.next=b
    return dummy.next
interval=1
l_len=len(lists)
while l_len>interval:
    for i in range(0,l_len-interval,2*interval):
        lists[i]=merge2Lists(lists[i],lists[i+interval])
    interval*=2
return lists[0] if lists else None

```

# 链表反转题
LC 206 Reverse Linked List

**全反转的经典代码**
```python
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        prev, cur, nxt = None, head, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
```

下面我们具体解释如何实现。使用三个指针变量 pre、curr、next 来记录反转的过程中需要的变量，它们的意义如下：

curr：指向待反转区域的第一个节点 left；

next：永远指向 curr 的下一个节点，循环过程中，curr 变化以后 next 会变化；

pre：永远指向待反转区域的第一个节点 left 的前一个节点，在循环过程中不变。

**反转部分的经典代码**
穿针法的经典代码，跟下面的那个找到头尾反转中间不同。
穿针法的核心就是保留好头指针
```python
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next#容易写成cur.next出错!!!
            pre.next = next
        return dummy_node.next
```

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/


反转K个一级链表

这个算法的思想是找到头尾后再反转中间
```python
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_linked_list(head: ListNode):
            # 也可以使用递归反转一个链表
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        # 因为头节点有可能发生变化，使用虚拟头节点可以避免复杂的分类讨论
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        # 第 1 步：从虚拟头节点走 left - 1 步，来到 left 节点的前一个节点
        # 建议写在 for 循环里，语义清晰
        for _ in range(left - 1):
            pre = pre.next

        # 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next
        # 第 3 步：切断出一个子链表（截取链表）
        left_node = pre.next
        curr = right_node.next

        # 注意：切断链接
        # pre.next = None#非必要
        right_node.next = None#必要

        # 第 4 步：同第 206 题，反转链表的子区间
        reverse_linked_list(left_node)
        # 第 5 步：接回到原来的链表中
        pre.next = right_node
        left_node.next = curr
        return dummy_node.next
```
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
