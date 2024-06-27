import string
import math

# ex 1
str_1 = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
         "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
         "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
         "It has survived not only five centuries, but also the leap into electronic typesetting, "
         "remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset "
         "sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like "
         "Aldus PageMaker including versions of Lorem Ipsum.")

# def get_avg_length_of_words(text):
#     count_words = 0
#     count_char = 0
#     words = text.split()
#
#     for word in words:
#         count_char += len(word.strip(string.punctuation))
#         count_words += 1
#     return count_char / count_words
#
#
# print(get_avg_length_of_words(str_1))


# ex 2
# nums = [1, 5, 4, 2]
#
# p = math.prod(nums)
# answer = [p // i for i in nums]
# print(answer)


# ex 3
# nums = [1, 5, 2, 8, 5, 6, 5, 2, 9, 6]
# lst = []
# for i in range(1, len(nums) + 1):
#     if i not in nums:
#         lst.append(i)
#
# print(lst)


# nums = [1, 5, 2, 8, 5, 6, 5, 2, 9, 6]
# nums_set = set(nums)
# all_numbers = set(range(1, len(nums) + 1))
# lst = list(all_numbers - nums_set)
#
# print(lst)
#
# import random
# a = 10
# b = 20
#
# print(random.uniform(a, b))
# print(random.random() * (b - a) + a)

