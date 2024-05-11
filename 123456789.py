# Словарь шифрования
# Словарь для шифрования
cipher = {
    'd': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e',
    'i': 'f', 'j': 'g', 'k': 'h', 'l': 'i', 'm': 'j',
    'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n', 'r': 'o',
    's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't',
    'x': 'u', 'y': 'v', 'z': 'w', 'a': 'x', 'b': 'y', 'c': 'z'
}


def encrypt_string(s, n):
    # Функция для шифрования строки один раз
    def encrypt_once(input_string):
        return ''.join(cipher.get(char, char) for char in input_string)

    # Шифрование строки n раз
    for _ in range(n):
        s = encrypt_once(s)
    return s


# Ввод данных пользователем
original_string = input("Введите строку для шифрования: ")
number_of_times = int(input("Введите количество повторений шифра: "))

# Получение и вывод зашифрованной строки
encrypted_string = encrypt_string(original_string, number_of_times)
print(f"Зашифрованная строка: {encrypted_string}")
