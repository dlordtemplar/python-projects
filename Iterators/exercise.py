# Version 1
# result = 0
# lis = [1, 2, 3]
# for x in lis:
#     for y in lis:
#         result += x * y
# # print(result)
#
# # Converted
# result2 = 0
# lis = [1, 2, 3]
# x_index = 0
# y_index = 0
# while x_index < len(lis):
#     while y_index < len(lis):
#         result2 += lis[x_index] * lis[y_index]
#         y_index += 1
#     x_index += 1
#     y_index = 0
# # print(result2)
# assert result == result2
#
# # Version 2
# result3 = 0
# it = iter([1, 2, 3])
# for x in it:
#     for y in it:
#         result3 += x * y
# # print(result3)
#
# result4 = 0
# it = iter([1, 2, 3])
# while True:
#     try:
#         x1 = next(it)
#         while True:
#             try:
#                 y1 = next(it)
#                 result4 += x1 * y1
#             except StopIteration:
#                 break
#     except StopIteration:
#         break
# # print(result4)
# assert result3 == result4
#
# # lis = [1, 2, 3]
# # for x in lis:
# #     lis.append(x)
# #     print(lis)
#
# str = "test"
# print(str.copy())


# F = (( C * 9 ) / 5 ) + 32
# print([(x, (x * 9 / 5) + 32) for x in [i * 5 for i in range(0, 20)]])


# def f1(words):
#     result = []
#     for word in words:
#         wordlenpair = (word, len(word))
#         result.append(wordlenpair)
#     return result
#
# def f2(words):
#     '''
#     >>> f2(['Python', 'is', 'great']
#     [('Python', 6), ('is', 2), ('great', 5)]
#     '''
#     return [(y, len(y)) for y in words]
#
# print(f2(['Python', 'is', 'great']))

for x in range(10, 1, -1):
    print(x)
