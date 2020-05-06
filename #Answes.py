def sort(dic):
    a=[]
    for i in sorted (dic) : 
        a.append(dic[i])
    return a
tb,tl,td=map(int,input().split())
dic={};sc={}
xyz=list(map(int,input().split()))
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
    t=list(map(int,input().split()))
    sup.append(t[1])
    if(t[1] in st.keys()):
        st[t[1]].append(i)
    else:
        st[t[1]]=[i]
    a=list(map(int,input().split()))
    dic2={}
    for j in a:
        dic2[dic[j]]=j
    ab=sort(dic2)
    #print(i)
    t.append(ab[::-1])
    lib[i]=t
sup.sort()
for i in st.keys():
    st[i].append(0)
book={};d=0
lib2=[];
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
