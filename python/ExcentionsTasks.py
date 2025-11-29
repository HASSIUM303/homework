# Задание 1

list1 = [1, 2, 3, 4, 5]
sum = 0

try:
    for i in list1:
        sum += i
except TypeError as e:
    print(f"Ошибка типизации: {e}")
except Exception as e:
    print(f"Ошибка: {e}")
else:
    print(sum)

# Задание 3

#list1 = [1,2,3,4,5,6,7,8,9,11]
list1 = []

try:
    print("Максимум: ", max(list1))
    print("Минимум: ", min(list1))
except Exception as e:
    print("Исключение: ", e)

# Задание 6

strings = [
    "1", "2", "3", "4", "5"
]
result = ""
try:
    for i in strings:
        result += i + " "
except Exception as e:
    print("Исключение: ", e)
else:
    print(result)