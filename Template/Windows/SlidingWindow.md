```python
def SlidingWindow(source,target):
    import collections
    need,window=collections.Counter(source),collections.Counter()
    left,right=0,0
    while(right<len(source)):
        w_right=source[right]# windows right
        right+=1
        # windows data update start

        # windows data update end
        # DEBUG here
        # print("window interval:[{},{}]".format(left,right))
        while(windows need shrink):
            w_left=source[left]
            left+=1
            # windows data update start
            
             # windows data update end
```