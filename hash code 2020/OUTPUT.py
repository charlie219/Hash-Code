from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import sys
import os
int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

stdin = open(os.path.join(sys.path[0],'f_libraries_of_the_world.txt'),'r')
sys.stdout = open(os.path.join(sys.path[0],'f.txt'),'w') # input1.in
    #solution

tb,tl,td=multi_int_input()
dic={};sc={}
xyz=list_input()
for i in range(len(xyz)):
    dic[i]=xyz[i]
    if(xyz[i] in sc.keys()):
        sc[xyz[i]].append(i)
    else:
        sc[xyz[i]]=[i]
xyz.sort()
for i in sc.keys():
    sc[i].append(0)
check={}
lib={};st={};sup=[]
for i in range(tl):
    t=list_input()
    sup.append(t[1])
    if(t[1] in st.keys()):
        st[t[1]].append(i)
    else:
        st[t[1]]=[i]
    a=list_input()
    ab=sorted([dic[i] for i in a],reverse=True)
    abc=[sc[i] for i in ab]
    t.append(a)
    lib[i]=t
sup.sort()
for i in st.keys():
    st[i].append(0)
book={};d=0
lib2=[]
for i in range(tl):
    t=[]
    lb=st[sup[i]][st[sup[i]][-1]]
    st[sup[i]][-1]+=1
    boo=[]
    for i in lib[lb][3]:
        if(i in book.keys()):
            continue
        boo.append(i)
        book[i]=0
    if(len(boo)<1):
        continue
    t.append(lb)
    t.append(len(boo))
    t.append(boo)
    lib2.append(t)
print(len(lib2))
for i in range(len(lib2)):
    print(lib2[i][0],lib2[i][1])
    print(*lib2[i][2])
#print(ti()-start)

