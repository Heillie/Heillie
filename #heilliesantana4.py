#heilliesantana
number= int(input("Please enter an undefined amount of numbers"))
numbers = []
numbers.append(number)

while (number!=0):
    number= int(input("Please enter an undefined amount of numbers"))
    numbers.append(number)
    
Sum = sum(numbers)
print(Sum)