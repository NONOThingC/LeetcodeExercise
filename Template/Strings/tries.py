


# {1,2,2,3,4,5,3,3,3,4,5}
from requests import head


cnt=0
new_head=head
ans=[]
i=0
L=1
while new_head.next:
    if new_head.next.val!=new_head.val:
        ans.append(i)
    i+=1
    L+=1
ans.append(L)

dummy=ListNode()
dummy.next=head

j=0
for i in range(L):
    if ans[j]==i:
        reverse(head,ans[j],ans[j+1])
        j+=1
