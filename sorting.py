# bubble_sort(), selection_sort() a random_numbers()

import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

# values = random_numbers(10)  # 10 čísel v rozsahu 0–100
# print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

# small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
# print(small)
# for i in range(len(values)):
#    min_num = i
#
#    for j in range(i + 1, len(values)):
#        if values[j] < values[min_num]:
#            min_num = j
#    values[i], values[min_num] = values[min_num], values[i]
#
# print(values)
# list = [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
# # def selection_sort(list):
# #     return sorted_list
# list = list[:]
# for pozice in range(len(list)):
#     min_idx = pozice
#     for projita in range(pozice + 1, len(list)):
#         if list[projita] < list[min_idx]:
#             min_idx = projita
#     list[pozice], list[min_idx] = list[min_idx], list[pozice]

def selection_sort(list):
    list = list[:]
    for pozice in range(len(list)):
        min_idx = pozice
        for projita in range(pozice + 1, len(list)):
            if list[projita] < list[min_idx]:
                min_idx = projita
        list[pozice], list[min_idx] = list[min_idx], list[pozice]
    return list



