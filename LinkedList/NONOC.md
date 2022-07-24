# 链表的初始值
可以用一个`dummy=LinkedList()`表达初值，
最后返回`dummy.next`即可。

# 链表题解法思路
双指针，快慢指针，考虑把链表相连或者接成环状。

# 链表交换题的思路
交换题只有下面三个要点：
1.一般来说，交换链表的题需要三个指针，领先于所交换范围的h,处于交换前一位置的pre，处于交换位置的cur，交换范围之后的tmp。只交换一次的只需要两个指针。

2.如果用了上述三个指针，那么循环判断条件该是：
```python
while cur and cur.next:
```
如果是只要两个指针的，通常一个判断条件即可。
```python
while cur.next:
```

3.头指针前添加一个dummy，以防止涉及第一个节点的交换出错。
```python
dummy=ListNode()
dummy.next=head
h=dummy
pre=dummy
cur=dummy.next
```