# ask user to input less than or equal to 6 numbers
number = int(input("Enter 6 or less digits: "))

#update value of num with the proper format
number = f"{number: 6d}"
#print number
print(number)
