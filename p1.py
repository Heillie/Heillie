#heilliesantana
b = "1,2,3,4,5"
numbers = sorted(map(int, b.split(',')))
result = ','.join(map(str, numbers))
print(result)
