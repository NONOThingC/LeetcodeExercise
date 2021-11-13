def gen_permutation(n=0,p_list=None):
    """
    generate permutation by n or list.
    """
    memo=[]
    res=[]
    def backtrack(n_list):
        if len(n_list)==1:
            return n_list[0]
        for i,ele in enumerate(n_list):
            tmp=[ele,]
            result=backtrack(n_list[:i]+n_list[i+1:])
            tmp.append(result)
            res.append(tmp)
        return 
    if p_list is not None:
        pass
    if n<1:
        return 