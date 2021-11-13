# binary tree to sequence
## Preorder traversal
```python
def Serialize(root->TreeNode,sep=",",NULL="#"):
    """
    tree to str
    """
    ans_str=""
    eles=[]
    def preorder_tra(root):
        locals eles
        locals sep
        locals NULL
        if (root == null):
            eles.append(NULL)
            return None
        eles.append(root.val)
        preorder_tra(root.left)
        preorder_tra(root.right)
    preorder_tra(root)
    ans_str=sep.join(eles)
    return ans_str
}

def deserialize(str_seq,sep=",",NULL="#"):
    eles=str_seq.strip().split(sep)
    root=TreeNode()
    ans_tree=TreeNode()
    link_list=root
    for ele in eles:
        link_list.left=TreeNode(val=ele)
        link_list=link_list.left

    /* 辅助函数，通过 nodes 列表构造二叉树 */
    def preorder_tra(root) {
        ans_tree=TreeNode()
        if root==NULL or root == None:
            return None
        ans_tree=root
        ans_tree.left=preorder_tra(root.left)
        ans_tree.right=preorder_tra(root.left)
        return ans_tree
    return preorder_tra(ans_tree)
解码框架没写对

```