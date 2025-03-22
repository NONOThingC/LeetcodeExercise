class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_len=len(s)
        valid=len(words)
        w_len=len(words[0])
        windows_len=valid*w_len
        
        
        
        ans=[]
        for st in range(w_len):
            i=st
            word2cnt=collections.Counter(words)
            rec=0
            while i < len(s)-windows_len+1:
                if i==st:
                    j=st
                    for _ in range(valid):
                        cur_s=s[j:j+w_len]
                        if  cur_s in words:
                            word2cnt[cur_s]-=1
                        if word2cnt.get(cur_s,-1)==0:
                            rec+=1
                        j+=w_len
                    if len(word2cnt)==rec:
                        ans.append(i)
                else:

                    last_s=s[i-w_len:i]
                    if word2cnt.get(last_s,-1)==0:
                        rec-=1
                    if  last_s in words:
                        word2cnt[last_s]+=1

                    cur_s=s[i+windows_len-w_len:i+windows_len]
                    if  cur_s in words:
                        word2cnt[cur_s]-=1
                    if word2cnt.get(cur_s,-1)==0:
                        rec+=1
                    if len(word2cnt)==rec:
                        ans.append(i)
                    
                i+=w_len
        return sorted(ans)