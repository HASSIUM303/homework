import string_utils
import random_utils
import constants

def test_string_utils():
    print("--- Тестирование модуля string_utils ---")
    my_string = "А роза упала на лапу Азора"
    
    upper_string = string_utils.to_upper(my_string)
    print(f"Строка в верхнем регистре: {upper_string}")
    
    char_count = string_utils.count_chars(my_string)
    print(f"Количество символов в строке: {char_count}")
    
    is_pal = string_utils.is_palindrome(my_string)
    print(f"Является ли строка палиндромом: {is_pal}")
    
    not_pal_string = "Привет, мир"
    is_pal_2 = string_utils.is_palindrome(not_pal_string)
    print(f"Является ли '{not_pal_string}' палиндромом: {is_pal_2}")
    print("-" * 20)

def test_random_utils():
    print("\n--- Тестирование модуля random_utils ---")
    rand_int = random_utils.random_integer(10, 20)
    print(f"Случайное целое число от 10 до 20: {rand_int}")
    
    rand_list = random_utils.random_list(5, 1, 100)
    print(f"Случайный список из 5 элементов: {rand_list}")
    
    shuffled = random_utils.shuffle_list(rand_list)
    print(f"Перемешанный список: {shuffled}")
    print(f"Оригинальный список не изменился: {rand_list}")
    print("-" * 20)

def test_constants():
    print("\n--- Тестирование модуля constants ---")
    print(f"Число Пи: {constants.PI}")
    print(f"Скорость света (м/с): {constants.SPEED_OF_LIGHT}")
    print(f"Гравитационная постоянная: {constants.GRAVITATIONAL_CONSTANT}")
    
    # Пример использования констант
    radius = 5
    circle_area = constants.PI * (radius ** 2)
    print(f"Площадь круга с радиусом {radius} равна: {circle_area}")
    
    mass = 1000 # кг
    energy = mass * (constants.SPEED_OF_LIGHT ** 2)
    print(f"Энергия, заключенная в массе {mass} кг (E=mc^2): {energy} Дж")
    print("-" * 20)

def main():
    test_string_utils()
    test_random_utils()
    test_constants()

if __name__ == "__main__":
    main()