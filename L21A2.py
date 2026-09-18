test_dict = {'Codingal': 8, 'is': 8, 'best': 2, 'for': 8,
             'Coding': 8, 'students': 1, 'to': 8, 'learn': 8, 'Python': 8, 'programming': 8, 'language': 8, 'is': 8, 'the': 8, 'best': 2, 'platform': 8, 'for': 8, 'learning': 8, 'Python': 8, 'programming': 8, 'language': 8, 'is': 8, 'the': 8, 'best': 2, 'platform': 8, 'for': 8, 'learning': 8, 'Python': 8, 'programming': 8, 'language': 8}

print("The original dictionary:" + str(test_dict))

x = 8

res = 0
for key in test_dict:
    if test_dict[key] == x:
        res = res + 1

print("Frequency of " + str(x) + ": " + str(res))
