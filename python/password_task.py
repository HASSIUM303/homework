import random
import string

def generate_password(length=8, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=False):
    chars = []
    if use_uppercase:
        chars.extend(string.ascii_uppercase)
    if use_lowercase:
        chars.extend(string.ascii_lowercase)
    if use_digits:
        chars.extend(string.digits)
    if use_special_chars:
        chars.extend(string.punctuation)
    if not chars:
        raise ValueError("Нужно выбрать хотя бы одну группу символов.")
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_password_strength(password):
    strength = {
        'length': len(password),
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digits': any(c.isdigit() for c in password),
        'special': any(c in string.punctuation for c in password)
    }
    score = sum(strength.values())
    if score >= 4 or (strength['length'] > 12 and score >= 3):
        return "Высокая"
    elif score >= 3 or (strength['length'] > 8 and score >= 2):
        return "Средняя"
    else:
        return "Низкая"

def generate_unique_passwords(count=1, length=8, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=False):
    passwords = set()
    while len(passwords) < count:
        new_pass = generate_password(length=length, use_uppercase=use_uppercase, use_lowercase=use_lowercase, use_digits=use_digits, use_special_chars=use_special_chars)
        passwords.add(new_pass)
    return list(passwords)

if __name__ == "__main__":
    generated_password = generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True)
    print(f"Сгенерированный пароль: {generated_password}")
    reliability = check_password_strength(generated_password)
    print(f"Уровень надежности: {reliability}")
    unique_passwords = generate_unique_passwords(count=5, length=10)
    print("\nСписок уникальных паролей:")
    for pwd in unique_passwords:
        print(pwd)
