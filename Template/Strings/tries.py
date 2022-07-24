
class Node():
    def __init__(self,val=None) -> None:
        self._child={}#char to Node
        self._value=val
    
    def _add_child(self,char,val,overwrite=False):
        child=self._child.get(char)
        if child is None:
            child=Node(value)
            self._child[char]=child
        elif overwrite:
            self._value=val
        return child
    
    def visit_child(self,child,char):
        return child._child.get(char)
    
    

class Tries(Node):
    def __init__(self, val=None) -> None:
        super().__init__(val)
        
    def __contains__(self,key):
        return self[key] is not None
    
    def __getitem__(self,key):
        state=self
        for char in key:
            state=state._child.get(char)
            if state==None:
                return None
        return state._value
        
    def __setitem__(self,key,value):
        state=self
        for i,char in enumerate(key):
            if i<len(key)-1:
                state=state._add_child(char,None,False)
            else:
                state=state._add_child(char,value,True)
                
    def to_prefix_node(self,string):
        """_summary_
        to prefix node in string, if not exist such prefix, return None
        Args:
            string (_type_): _description_
        """
        child=self
        for char in string:
            child=self.visit_child(child,char)
        return char
    
    

                
prefixTree=Tries()
s="我爱自然语言处理"
t=["我","爱","自然","自然语言","处理"]
for key,value in zip(t,[1]*len(t)):#1表示leaf
    prefixTree[key]=value

def scan(s,prefixTree):
    p=0
    ans=[]
    while p<len(s):
        start=p
        child=prefixTree
        while p<len(s) and child.visit_child(child,s[p]) is not None:
            child=child.visit_child(child,s[p])
            p+=1
        if start==p:
            ans.append(s[p])
            p+=1
        else:
            ans.append(s[start:p])
    return ans
print(scan(s,prefixTree))


## another version：Nodes are replaced by dictionary. is_word is replaced by adding a "-" key to the dictionary. 

class Trie(object):

	def __init__(self):
		self.trie = {}


	def insert(self, word):
		t = self.trie
		for c in word:
			if c not in t: t[c] = {}
			t = t[c]
		t["-"] = True


	def search(self, word):
		t = self.trie
		for c in word:
			if c not in t: return False
			t = t[c]
		return "-" in t

	def startsWith(self, prefix):
		t = self.trie
		for c in prefix:
			if c not in t: return False
			t = t[c]
		return True

