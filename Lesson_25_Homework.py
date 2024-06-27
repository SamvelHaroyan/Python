# # ex 2
# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 = {}
# for i in dict_1.values():
#     dict_2[i] = len(i)
#
# print(dict_2)
import random

# print(dict(map(lambda x: (x, len(x)), dict_1.values())))


# # ex 3
# dict_1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
#
# # first variant
# dict_2 = {}
# for i, j in dict_1.items():
#     dict_2[i] = list(filter(lambda x: x % 2 != 0, j))
#
# # second variant
# dict_2 = dict(map(lambda item_tpl: (item_tpl[0], list(filter(lambda x: x % 2 != 0, item_tpl[1]))), dict_1.items()))
#
# print(dict_2)
#




