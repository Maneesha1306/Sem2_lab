f1=open("file1.txt","r")
f2=open("file2.txt","w")
cont=f1.readlines()
for i in range(len(cont)):
    if i%2==0:
        f2.write(cont[i])
f1.close()
f2.close()
f2=open("file2.txt","r")
cont=f2.read()
print(cont)
f2.close()
