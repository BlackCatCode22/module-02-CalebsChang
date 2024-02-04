# input of three numbers
num = input("Enter the first Number: ")
num2 = input("Enter the second Number: ")
num3 = input("Enter the third Number: ")

if num >= num2:
    if num >= num3:
        large = num
    else:
        large = num3
else:
    if num2 >= num3:
        large = num2
    else:
        large = num3
print("The largest number is:", large)
