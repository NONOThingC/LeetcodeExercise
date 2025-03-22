citations=[2,1,5,7,2,3,1,6,0]

#维护一个出现次数的列表
value2cnt=[0]*(max(citations)+1)
for citation in citations:
    value2cnt[citation]+=1
    
#维护一个对于每个值出现次数的前缀和
value2cum_cnt=[0]*(max(citations)+1)#注意要多一个是因为有0
value2cum_cnt[0]=value2cnt[0]
for i in range(1,len(value2cnt)):
    value2cum_cnt[i]=value2cum_cnt[i-1]+value2cnt[i]

#注意是倒着找，倒着把数组末尾值放到该放的地方上
ans=[0]*len(citations)
for i in range(len(citations)-1,-1,-1):
    ele=citations[i]
    value2cum_cnt[ele]-=1    
    ans[value2cum_cnt[ele]]=citations[i]