a=int(input())
marksheet=[]
score=[]
for i in range(a):
    n = input()
    s = float(input())
    marksheet+=[[n,s]]
    score+=[s]
b=sorted(list(set(score)))[1]
l=[]
for c,d in marksheet:
    if d==b:
        l.append(c)
for i in sorted(l):
    print(i)
