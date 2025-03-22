本节讲了数位 DP 的通用模板，以及如何使用该模板秒杀相关困难题目。
讲完题目后还讲了一些上分的训练技巧。

将 nn 转换成字符串 ss，定义 f(i,\textit{mask}, \textit{isLimit},\textit{isNum})f(i,mask,isLimit,isNum) 表示构造从左往右第 ii 位及其之后数位的合法方案数，其余参数的含义为：

\textit{mask}mask 表示前面选过的数字集合，换句话说，第 ii 位要选的数字不能在 \textit{mask}mask 中。
\textit{isLimit}isLimit 表示当前是否受到了 nn 的约束。若为真，则第 ii 位填入的数字至多为 s[i]s[i]，否则可以是 99。如果在受到约束的情况下填了 s[i]s[i]，那么后续填入的数字仍会受到 nn 的约束。
\textit{isNum}isNum 表示 ii 前面的数位是否填了数字。若为假，则当前位可以跳过（不填数字），或者要填入的数字至少为 11；若为真，则必须填数字，且要填入的数字可以从 00 开始。
后面两个参数可适用于其它数位 DP 题目。

枚举要填入的数字，具体实现逻辑见代码。

下面代码中 Java/C++/Go 只需要记忆化 (i,\textit{mask})(i,mask) 这个状态，因为：

对于一个固定的 (i,\textit{mask})(i,mask)，这个状态受到 \textit{isLimit}isLimit 或 \textit{isNum}isNum 的约束在整个递归过程中至多会出现一次，没必要记忆化。
另外，如果只记忆化 (i,\textit{mask})(i,mask)，\textit{dp}dp 数组的含义就变成在不受到约束时的合法方案数，所以要在 !isLimit && isNum 成立时才去记忆化。
```
附：力扣上的数位 DP 题目
233. 数字 1 的个数（题解）
面试题 17.06. 2出现的次数（题解）
600. 不含连续1的非负整数（题解）
902. 最大为 N 的数字组合（周赛精讲 中讲了）
1012. 至少有 1 位重复的数字
1067. 范围内的数字计数
1397. 找到所有好字符串（有难度，需要结合一个知名字符串算法）
。

```


```python
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = f(i + 1, mask, False, False)
            up = int(s[i]) if is_limit else 9
            for d in range(0 if is_num else 1, up + 1):  # 枚举要填入的数字 d
                if mask >> d & 1 == 0:  # d 不在 mask 中
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res
        return f(0, 0, True, False)

```
