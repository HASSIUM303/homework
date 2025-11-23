# Задание 1
virajenie = input("Введите арифметическое выражение: ")

if '+' in virajenie:
    chasti = virajenie.split('+')
    chislo1 = int(chasti[0])
    chislo2 = int(chasti[1])
    resultat = chislo1 + chislo2
elif '-' in virajenie:
    chasti = virajenie.split('-')
    chislo1 = int(chasti[0])
    chislo2 = int(chasti[1])
    resultat = chislo1 - chislo2
elif '*' in virajenie:
    chasti = virajenie.split('*')
    chislo1 = int(chasti[0])
    chislo2 = int(chasti[1])
    resultat = chislo1 * chislo2
elif '/' in virajenie:
    chasti = virajenie.split('/')
    chislo1 = int(chasti[0])
    chislo2 = int(chasti[1])
    if chislo2 != 0:
        resultat = chislo1 / chislo2
    else:
        resultat = "Ошибка: деление на ноль"
else:
    resultat = "Неизвестная операция"

print("Результат:", resultat)

# Задание 2
import random

spisok = []
for i in range(20):
    spisok.append(random.randint(-10, 10))

print("Список чисел:", spisok)

min_chislo = spisok[0]
max_chislo = spisok[0]

for chislo in spisok:
    if chislo < min_chislo:
        min_chislo = chislo
    if chislo > max_chislo:
        max_chislo = chislo

otric_count = 0
polozh_count = 0
nuli_count = 0

for chislo in spisok:
    if chislo < 0:
        otric_count += 1
    elif chislo > 0:
        polozh_count += 1
    else:
        nuli_count += 1