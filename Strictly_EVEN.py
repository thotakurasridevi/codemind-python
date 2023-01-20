n=int(input())
l=list(map(int,input().split()))
d=[]
e=[]
for i in range(len(l)):
    if l[i]%2==0 and i%2==0:
        d.append(i)
for j in l:
    if j%2==0:
        e.append(j)
if len(d)==len(e):
    print("True")
else:
    print("False")