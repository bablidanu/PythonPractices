# Program to find the sum of digits of a number

#step 1 : Take input from the user
num = int(input("Enter a number: "))

#Step 2 : Convert to string and iterate through each digit

digit_sum = sum(int(digit) for digit in str(num))

#step 3 : Print the result
print("The sum of digits is:", digit_sum)