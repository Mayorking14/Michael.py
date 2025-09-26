numbers = {1,2,4,8,16} | {1,4,16,64,256} #union
numbers2 = {1,2,4,8,16} & {1,4,16,64,256} #intersection
numbers3 = {1,2,4,8,16} - {1,4,16,64,256} #minus or difference
#numbers4 = {1,2,4,8,16}  {1,4,16,64,256}
numbers5 = {1,2,4,8,16} > {1,4,16,64,256}
print(sorted(numbers))
print(sorted(numbers2))
print(sorted(numbers3))
print(numbers5)