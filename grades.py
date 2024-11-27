a=int(input("enter the marks obtained in subject 1:"))
b=int(input("enter the marks obtained in subject 2:"))
c=int(input("enter the marks obtained in subject 3:"))
d=int(input("enter the marks obtained in subject 4:"))
e=int(input("enter the marks obtained in subject 5:"))
tot=a+b+c+d+e
per=(tot/500)*100
if per>=80:
    print("Grade A")
elif per>=70:
    print("Grade B")
elif per>=60:
    print("grade C")
elif per>=40:
    print("Grade D")
else:
    print("Grade E")
    
