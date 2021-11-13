# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:40:13 2021

@author: 11457
"""
import collections
import copy
matrix=[[0 for y in range(4)] for x in range(5)]
last_matrix=[[0 for y in range(4)] for x in range(5)]
results_matrix=[]
reward_matrix=collections.defaultdict(int)
reward_matrix[(4,3),"r"]=1
reward_matrix[(4,3),"u"]=1
reward_matrix[(4,3),"d"]=1
reward_matrix[(4,3),"l"]=1
reward_matrix[(4,2),"r"]=-1
reward_matrix[(4,2),"u"]=-1
reward_matrix[(4,2),"d"]=-1
reward_matrix[(4,2),"l"]=-1


beta=0.9
direction2num={"u":(0,1),"d":(0,-1),"l":(-1,0),"r":(1,0)}
def f(x,min_val=1,max_val=4):
    return min(max(x,min_val),max_val)

def g(x):
    return min(max(x,1),3)



def direction_max(x,y,dir_string="udlr",mid_walls=()):
    "检查dir_string中方向的值并得到最大值。"
    ans=float("-inf")
    for direction in dir_string:
        if direction in "udlr":
            vert_dir=[(int(not direction2num[direction][0]),int(not direction2num[direction][1])),(-int(not direction2num[direction][0]),-int(not direction2num[direction][1]))]
            cur_x,cur_y=(x,y) if (x+direction2num[direction][0],y+direction2num[direction][1]) in mid_walls else (x+direction2num[direction][0],y+direction2num[direction][1])
            vert_x2,vert_y2=(x,y) if (x+vert_dir[1][0],y+vert_dir[1][1]) in mid_walls else (x+vert_dir[1][0],y+vert_dir[1][1])
            vert_x1,vert_y1=(x,y) if (x+vert_dir[0][0],y+vert_dir[0][1]) in mid_walls else (x+vert_dir[0][0],y+vert_dir[0][1])
            ans=max(ans,reward_matrix[(x,y),direction]+beta*(0.8*last_matrix[f(cur_x)][g(cur_y)]+0.1*last_matrix[f(vert_x1)][g(vert_y1)]+0.1*last_matrix[f(vert_x2)][g(vert_y2)]))
        else:
            print("error direction!")
            exit(1)
    return ans



for i in range(10):
    for x in range(4,0,-1):
        for y in range(3,0,-1):
            if x==y and x==2:
                continue
            if x==4 and y==2 and i!=0:
                continue
            if x==4 and y==3 and i!=0:
                continue
            matrix[x][y]=direction_max(x,y,mid_walls=((2,2),))

    last_matrix=copy.deepcopy(matrix)
    results_matrix.append(last_matrix)


output = open('data.xls','w',encoding='gbk')

for result in results_matrix:
    for i in range(1,len(result)):
        for j in range(1,len(result[0])):
            output.write(str(result[i][j]))
            output.write('\t')
    output.write('\n')
output.close()     

     #写完一行立马换行


    
