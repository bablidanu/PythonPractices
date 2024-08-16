# finding the maximum number between two numbers using if else 
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

if a > b :
    print(f"Max value is : {a}")
else :
    print(f"Max value is : {b}")

#using function

def max(a,b):
    if a > b:
        return a
    else :
        return b
    
print(max(4,34))