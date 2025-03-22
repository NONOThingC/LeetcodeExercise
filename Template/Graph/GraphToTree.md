# leetcode:https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/

```java
class Solution {
    int mx = 0;
    vector<vector<int>> e;

    void dfs1(TreeNode *node) {
        if (node == nullptr) return;
        mx = max(mx, node->val);
        dfs1(node->left); dfs1(node->right);
    }

    void dfs2(TreeNode *node) {
        if (node->left != nullptr) {
            e[node->val].push_back(node->left->val);
            e[node->left->val].push_back(node->val);
            dfs2(node->left);
        }
        if (node->right != nullptr) {
            e[node->val].push_back(node->right->val);
            e[node->right->val].push_back(node->val);
            dfs2(node->right);
        }
    }
    //非常简洁的遍历方法，只要跟fa不等的节点就向下遍历
    int dfs3(int sn, int fa) {
        int ret = 0;
        for (int fn : e[sn]) if (fn != fa) ret = max(ret, dfs3(fn, sn) + 1);
        return ret;
    }

public:
    int amountOfTime(TreeNode* root, int start) {
        dfs1(root);
        e.resize(mx + 1);
        dfs2(root);
        return dfs3(start, -1);
    }
};
```


```python
num = n + 1
adj = [[] for _ in range(num)]

for i in range(n-1):
    a,b=list(map(int,input().split(" ")))
    adj[a].append(b)
    adj[b].append(a)

class Node:
    def __init__(self,val=None,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

class Node:
    def __init__(self,val=None,child=None) -> None:
        self.val=val
        self.child=None

#建树
head=Node(val=x,left=None,right=None)
visited=set()
def dfs(root):
    if root:
        visited.add(root.val)
        norep_adj=list(set(adj[root.val])-visited)
        adj_len=len(norep_adj)
        if adj_len==0:
            return None
        elif adj_len==1:
            root.left=Node(val=norep_adj[0])
            dfs(root.left)
            
        else:
            root.left=Node(val=norep_adj[0])
            dfs(root.left)
            root.right=Node(val=norep_adj[1])
            dfs(root.right)
dfs(head)
```