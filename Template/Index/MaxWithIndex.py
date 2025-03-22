def max_index(nums,st,end):
    #返回最大值及其对应的index,[st,end)
    ans=nums[st]
    idx=st
    for i in range(st+1,end):
        if nums[i]>=ans:#>=时值相同时尽量选靠后的，>是尽量选靠前的
            ans=nums[i]
            idx=i
    return ans,idx

def min_index(nums,st,end):
    #返回最大值及其对应的index,[st,end)
    ans=nums[st]
    idx=st
    for i in range(st+1,end):
        if nums[i]<=ans:#<=时值相同时尽量选靠后的，<是尽量选靠前的
            ans=nums[i]
            idx=i
    return ans,idx