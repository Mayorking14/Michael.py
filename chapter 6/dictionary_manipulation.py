dictionary = {
    'Canada': 'ca',
    'United States': 'us',
    'Mexico': 'me'
}
#check if canada in dictionary
print('Canada' in dictionary)

#check if france in dictionary
print('France' in dictionary)

#print in tabular form
for country, code in dictionary.items():
   print(f'{country:<14} {code}')

#add sweden
dictionary['Sweden'] = 'sw'
print(dictionary)

#update sweden
dictionary['Sweden'] = 'se'
print(dictionary)