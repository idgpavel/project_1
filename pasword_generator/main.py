import random
import string
import os


class password_generator:
    def __init__(self, length, emoji):
        self.length = length
        self.emoji = emoji
        # Заранее создается переменная, чтобы после генерации, можно было сохранить пароль
        self.password = ''
        # Стандартный набор символов, если человеку не нужен Unicode
        self.Lists = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Функция для генерации пароля с двумя режимами
    def generate(self):
        character_pool = self.Lists
        if self.emoji == 1:
            unicode_characters = ''.join(chr(i) for i in range(10000, 11000))
            character_pool += unicode_characters
        password = ''.join(random.choices(character_pool, k=self.length))
        self.password = password
        return password

    # Функция сохранения пароля в папку программы
    def save(self, website, login):
        os.makedirs(website, exist_ok=True)
        file_path = os.path.join(website, f"{login}.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Логин:\n{login}\n")
            file.write(f"Пароль:\n{self.password}\n")

def main():
    good = 0
    print("Запущен генератор паролей.")
    while good != 1:
        length = int(input("Введите длину пароля: "))
# Режим без Unicode я сделал, тк не все сайты принимают эти символы в качестве пароля, а также их ручной ввод затруднителен
        emoji = int(input("Если вы желаете использовать символы Unicode, введите: 1\nВ противном случае, введите: 0\n"))
        generator = password_generator(length, emoji)
        password = generator.generate()
        print(f"Ваш сгенерированный пароль: {password}")
        good = int(input("Если вы желаете довольны паролем, введите: 1\nВ противном случае, введите: 0\n"))
    save_f = int(input('Если вы желаете сохранить пароль, то введите: 1\nИначе введите: 0\n'))
    if save_f == 1:
        website = input('Введите название сайта\n')
        login = input('Введите логин аккаунта\n')
        generator.save(website, login)
        print('Пароль успешно сохранен в папке с названием указанного вебсайта')


if __name__ == "__main__":
    main()
