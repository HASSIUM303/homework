import random

text = input("Введи пример (например, 5+3): ")

if "+" in text:
    sign = "+"
elif "-" in text:
    sign = "-"
elif "*" in text:
    sign = "*"
elif "/" in text:
    sign = "/"
else:
    print("Я не понял знак! Используй +, -, * или /")
    exit()

if sign == "+":
    parts = text.split("+")
elif sign == "-":
    parts = text.split("-")
elif sign == "*":
    parts = text.split("*")
elif sign == "/":
    parts = text.split("/")


first = float(parts[0])
second = float(parts[1])


if sign == "+":
    answer = first + second
elif sign == "-":
    answer = first - second
elif sign == "*":
    answer = first * second
elif sign == "/":
    if second == 0:
        print("На ноль делить нельзя!")
        exit()
    else:
        answer = first / second

print("Ответ:", answer)

#Second

numbers = []
for i in range(10):
    numbers.append(random.randint(-50, 50))

min_num = numbers[0]
max_num = numbers[0]
negative_count = 0
positive_count = 0
zero_count = 0

for num in numbers:
   if num < min_num:
        min_num = num
   if num > max_num:
        max_num = num

   if num < 0:
        negative_count += 1
   elif num > 0:
        positive_count
   else: zero_count += 1 