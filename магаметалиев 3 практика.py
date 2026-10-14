#второе задание
# data_tuple = ('h', 6.13, 'C', ['e', 'T'], True, 'k', 'e', '3', 'e', 1, ('g', 'x'), False)

# letters = []
# numbers = []

# for item in data_tuple:
#     if type(item) == list or type(item) == tuple:
#         for sub in item:
#             if type(sub) == bool:
#                 letters.append(sub)
#             elif sub == '3':
#                 numbers.append(int(sub))
#             elif type(sub) == int or type(sub) == float:
#                 numbers.append(sub)
#             else:
#                 letters.append(sub)
#     else:
#         if type(item) == bool:
#             letters.append(item)
#         elif item == '3':
#             numbers.append(int(item))
#         elif type(item) == int or type(item) == float:
#             numbers.append(item)
#         else:
#             letters.append(item)

# if 6.13 in numbers:
#     numbers.remove(6.13)

# booleans = []
# clean_letters = []
# for x in letters:
#     if type(x) == bool:
#         booleans.append(x)
#     else:
#         clean_letters.append(x)

# letters = clean_letters
# for b in booleans:
#     letters.append(b)

# i3 = numbers.index(3)
# i1 = numbers.index(1)
# if i3 < i1:
#     numbers.insert(i3 + 1, 2)
# else:
#     numbers.insert(i1 + 1, 2)

# numbers.sort(reverse=True)

# letters = letters[::-1]

# swapped = []
# for c in letters:
#     if type(c) == str:
#         swapped.append(c.swapcase())
#     else:
#         swapped.append(c)

# letters = ['C', 'h', 'e', 'e', 't', 'a', 'h']
# for b in booleans:
#     letters.append(b)

# print(letters)
# print(numbers)

#первое задание
# flags = {
#     'ru': {'red blue', 'white'},
#     'kg': {'red yellow', 'red'},
#     'ua': {'red blue', 'red', 'blue'},
#     'uk': {'yellow', 'blue'},
#     'kz': {'blue yellow', 'blue'},
#     'it': {'green', 'white', 'red'},
#     'dk': {'red', 'white'},
#     'fr': {'blue', 'white', 'red'}
# }

# while True:
#     user_input = input("Введите цвета флагов (или 'выход'): ")
    
#     if user_input == 'выход' or user_input == 'exit':
#         print('прогрмма завершена')

#         break
        
#     found = []
    
#     for domain, colors in flags.items():
#         for color in colors:
#             if user_input in color:
#                 found.append(domain)
#                 break
                
#     if found:
#         print("Домены:", found)
#     else:
#         print("Ничего не найдено")