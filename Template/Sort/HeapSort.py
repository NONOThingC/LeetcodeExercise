

def heapify(arr,n,i):
    lchild,rchild=2*i+1,2*i+2
    largest=i
    if lchild<n and arr[lchild]>arr[largest]:
        largest=lchild
    if rchild<n and arr[rchild]>arr[largest]:
        largest=rchild
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def heapsort(arr):
    n=len(arr)
    #构建一个大顶堆，此时数组还没排好
    for i in range(n,-1,-1):
        heapify(arr,n,i)
    #每次将堆顶元素放入到最终位置上，于是就可以得到升序排列的数字了，放完后要调整堆。
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

arr=[12,11,13,-2,0,6]
for i in range(len(arr)):
    arr[i]=-arr[i]
heapsort(arr)
for i in range(len(arr)):
    print(f"{-arr[i]} ")
    
arr=[12,11,13,-2,0,6]
heap=[]