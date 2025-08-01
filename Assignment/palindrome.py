digits = int(input('input 5 digit integer: '))

result = digits // 10000
result1 = digits % 10000 // 1000
result2 = digits % 1000 // 100
result3 = digits % 100 // 10
result4 = digits % 10

print(result, result1, result2, result3, result4, end=' ')
