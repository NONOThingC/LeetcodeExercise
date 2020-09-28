def ZeroOnePack(arr:list,cost,value,volumn,aggregate=max():function):
    for v in range(volumn,cost-1):
        arr[v]=aggregate(arr[v],arr[v-cost]+value)

def ZeroOneSnapsack(Cost:list,Value:list,volumn,opt=1,just_full=0,aggregate=max:function):
    """
     可以这样理解：初始化数组事实上就是在没有任何物品可以放入背包时的合法状态。
     如果要求背包恰好装满，那么此时只有容量0的背包可以在什么也不装且价值0的情况下被“恰好装满”，
     其它容量的背包均没有合法的解，属于-∞未定义的状态，应该被赋值-∞。
     如果背包并非必须被装满，那么任何容量的背包,都有一个合法解“什么都不装”，
     这个解的价值0，所以初始时状态的值也就全部0了。
    """
    assert Cost==Value,"Error cost and value, please check."
    if just_full:
        arr=[0]+[-float("-inf")]*(volumn-1)
    else:
        arr=[0]*volumn
    if opt:
        cost_sum=sum(Cost)
        for i in range(len(Cost)):
            for j in range(volumn,min(cost_sum)-1):
                arr[v]=aggregate(arr[v],arr[v-])
    for i in range(len(Cost)):
        ZeroOnePack(arr,Cost[i],Value[i],volumn)

def CompletePack(arr:list,cost,value,volumn,aggregate=max()):
    for v in range(cost,volumn+1):
        arr[v]=aggregate(arr[v],arr[v-cost]+value)

