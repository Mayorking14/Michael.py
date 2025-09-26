def rotate(first,second,third):
    return (third,first,second)

first = 'doug'
second = 22
third = 1984
result = rotate(first,second,third)
print(result)

result2 = rotate(result[0],result[1],result[2])
print(result2)

result3 = rotate(result2[0],result2[1],result2[2])
print(result3)