print("Enter 'c' to convert celsius to fahrenheit")
print("Enter 'f' to convert fahrenheit to celsius")
choice=input("Enter your choice:")
if choice=='c':
    celsius=float(input('enter temperature in celsius:'))
    fahrenheit=(celsius*9/5)+32
    print("%.2f Celsius is: %0.2f Fahrenheit"%(celsius, fahrenheit))
elif choice=='f':
    fahrenheit=float(input("enter temperature in fahrenheit:"))
    celsius=(fahrenheit+32)*5/9
    print("%.2f Fahrenheit is: %0.2f Celsius"%(fahrenheit, celsius))
else:
    print("Invalid input")
    
