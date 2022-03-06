
```python
def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    pow = 1
    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow
```
x是底，n是幂，首先看`n<0`情况转化为`n>0`，然后就要对n进行分解了，n分解时候不直接乘n，而是让底数呈倍数增加，而让幂逐步一直除2直到为0。