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
