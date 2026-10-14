'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

temp_1 = float(input("Введите температуру Нарын: "))
temp_2 = float(input("Введите температуру Бишкек: "))
temp_3 = float(input("Введите температуру Ош: "))
temp_4 = float(input("Введите температуру Джалал-Абад: "))
temp_5 = float(input("Введите температуру Иссык-Куль: "))

total = temp_1 + temp_2 + temp_3 + temp_4 + temp_5
average = total / 5

average = round(average, 2)

print("Средняя температура на КР сегодня составляет ", average, " градусов цельсия")
