N=int(input("Enter N:"))
arr=[]
for i in range(N):
    arr.append(int(input("Enter element:")))
odd=0
even=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"No. of odd numbers:{odd}")
print(f"No. of even numbers:{even}")
