r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())
M1=[]
for i in range(r1):
    M1.append(list(map(int,input().split())))
M2=[]
for i in range(r2):
    M2.append(list(map(int,input().split())))
print("Matrix1")
for i in M1:
    print(i)
print("Matrix2")
for i in M2:
    print(i)
R=[]
if r1==r2 and c1==c2:
    R=[[[0]*c1]*r1]
    print("Result")
    print(R)
    for i in range(r1):#0,1,2
        for j in range(c1):#0,1
            s=M1[i][j]+M2[i][j]
            R[i][j]+=s
for i in R:
    print(i)