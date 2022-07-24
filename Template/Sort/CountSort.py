citations=[2,1,5,7,2,3,1,6,0]
score2cnt=[0]*(max(citations)+1)
for citation in citations:
    score2cnt[citation]+=1
s2cum_cnt=[0]*(max(citations)+1)
s2cum_cnt[0]=score2cnt[0]
for i in range(1,len(score2cnt)):
    s2cum_cnt[i]=s2cum_cnt[i-1]+score2cnt[i]

ans=[0]*len(citations)
for i in range(len(citations)-1,-1,-1):
    ele=citations[i]
    s2cum_cnt[ele]-=1    
    ans[s2cum_cnt[ele]]=citations[i]