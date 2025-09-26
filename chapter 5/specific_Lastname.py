# def name(names):
#     for name in names:
#         if names[name][1] == "jones":
#             return name
#
# names = [['hannah', 'jones'],
#         ['jones', 'jones'],
#         ['jones', 'mark'],
#         ['Mike', 'Robin'],
#         ['Robin', 'Mike'],
#          ]
# print(name(names))

names = [('hannah', 'jones'),
         ('jones', 'jones'),
         ('jones', 'mark'),
        ('Mike', 'Robin'),
        ('Robin', 'Mike'),
         ]

filtered = list(filter(lambda name: name[1] == 'jones', names))
print(filtered)