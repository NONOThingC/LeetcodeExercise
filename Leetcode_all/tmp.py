#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# {__name__}.py
# @Author : {__author__} ({__email__})
# @Link   : {__link__}
# @Date   : {__date__}
import typing
from typing import List, Optional, Tuple
import copy
from copy import deepcopy, copy
import collections
from collections import deque, defaultdict, Counter, OrderedDict, namedtuple
import math
from math import sqrt, ceil, floor, log, log2, log10, exp, sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
import bisect
from bisect import bisect_right, bisect_left
import heapq
from heapq import heappush, heappop, heapify, heappushpop
import functools
from functools import lru_cache, reduce, partial # cache
# cache = partial(lru_cache, maxsize=None)
# cache for Python 3.9, equivalent to @lru_cache(maxsize=None)
import itertools
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate
import string
from string import ascii_lowercase, ascii_uppercase
# s = ""
# s.isdigit, s.islower, s.isnumeric
import operator
from operator import add, sub, xor, mul, truediv, floordiv, mod, neg, pos # 注意 pow 与默认环境下的 pow(x,y, MOD) 签名冲突
import sys, os
# sys.setrecursionlimit(10000)
import re

# https://github.com/grantjenks/python-sortedcontainers
import sortedcontainers
from sortedcontainers import SortedList, SortedSet, SortedDict
# help(SortedDict)
# import numpy as np
from fractions import Fraction
from decimal import Decimal

# from utils_leetcode import testClass
# from structures import ListNode, TreeNode, linked2list, list2linked

def testClass(inputs):
    # 用于测试 LeetCode 的类输入
    s_res = [None] # 第一个初始化类, 一般没有返回
    methods, args = [eval(l) for l in inputs.split('\n')]
    class_name = eval(methods[0])(*args[0])
    for method_name, arg in list(zip(methods, args))[1:]:
        r = (getattr(class_name, method_name)(*arg))
        s_res.append(r)
    return s_res

""" 
https://leetcode.cn/contest/weekly-contest-261
https://leetcode-cn.com/contest/biweekly-contest-71
@2022 """
class Solution:
    """  """
    def largestMerge(self, word1: str, word2: str) -> str:
        ans=[]
        i,j=0,0
        l1,l2=len(word1),len(word2)
        while i<l1 or j<l2:
            tmp1,tmp2=i,j
            while tmp1<l1 and tmp2<l2 and word1[tmp1]==word2[tmp2]:
                tmp1+=1
                tmp2+=1
            if tmp1<l1 and tmp2<l2:
                if word1[tmp1]<word2[tmp2]:
                    ans.append(word2[j:tmp2+1])
                    j=(tmp2+1)
                elif word1[tmp1]>word2[tmp2]:
                    ans.append(word1[i:tmp1+1])
                    i=(tmp1+1)
            elif tmp1<l1:
                ans.append(word1[i:])
                i=l1
            elif tmp2<l2:
                ans.append(word2[j:])
                j=l2
            print(ans)
        return "".join(ans)
    
    
    
    
    

    
sol = Solution()
result=sol.largestMerge("cabaa","bcaaa")

for r in result:
    print(r)