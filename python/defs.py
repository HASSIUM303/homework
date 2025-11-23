# Задание 1
def display_quote():
    print("''Don't let the noise of others' opinions\n"
          "drown out your own inner voice.''\n"
          "- Steve Jobs")

# Задание 2
def numbers_between(a, b):
    for i in range(a + (a % 2 == 0), b, 2):
        print(i)

# Задание 3
def draw_line(length, direction='horizontal', char='*'):
    if direction == 'horizontal':
        print(char * length)
    elif direction == 'vertical':
        for _ in range(length):
            print(char)

# Задание 4
def max_of_four(a, b, c, d):
    return max(a, b, c, d) #Мда

# Задание 5
def sum_range(start, end):
    total = 0
    for num in range(start, end+1):
        total += num
    return total

# Задание 6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Задание 7
def is_lucky_number(number):
    number_str = str(number)
    
    first_part = int(number_str[0]) + int(number_str[1]) + int(number_str[2])
    second_part = int(number_str[3]) + int(number_str[4]) + int(number_str[5])

    return first_part == second_part