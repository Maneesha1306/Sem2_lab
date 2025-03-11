num=int(input("Enter the elements in the dictionary : ")) 
my_dict={} 
for x in range(num): 
    key=input(f"Enter key : ") 
    value=int(input(f"Enter value : ")) 
    my_dict[key]=value 
total = sum(my_dict.values()) 
print("My Dictionary : ",my_dict) 
print("Total : ",total) 