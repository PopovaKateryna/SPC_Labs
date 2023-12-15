import art
from termcolor import colored2 

class ArtManager:
    def get_art(self, font_name, text):
        try:
            return art.text2art(text, font=font_name)
        except Exception as e:
            print(f"Помилка: {e}")
            return art.text2art(text, font='block')

class ColorManager:
    def __init__(self):
        self.colors = {
            'червоний': 'red',
            'синій': 'blue',
            'зелений': 'green'
        }

    def get_color(self):
        color_name = input("Виберіть колір тексту (червоний/синій/зелений): ").lower()
        return self.colors.get(color_name, 'white')

class SizeManager:
    def get_size(self):
        try:
            width = int(input("Введіть ширину ASCII-арту: "))
            height = int(input("Введіть висоту ASCII-арту: "))
        except ValueError:
            width, height = 80, 20
        return width, height

class FileManager:
    def save_art(self, formatted_art):
        file_name = input("Введіть ім'я файлу для збереження: ")
        with open(file_name, 'w') as file:
            file.write(formatted_art)
            print(f"ASCII-арт був збережений у файлі '{file_name}'")

class AsciiArtGenerator:
    def __init__(self):
        self.art_manager = ArtManager()
        self.color_manager = ColorManager()
        self.size_manager = SizeManager()
        self.file_manager = FileManager()

    def get_user_input(self, prompt, default=None):
        user_input = input(prompt).strip()
        return user_input if user_input else default

    def run(self):
        text = self.get_user_input("Введіть слово або фразу для генерації ASCII-арту: ")
        font_name = self.get_user_input("Виберіть шрифт (стандартний/керований/блоки): ", default='block')
        art_object = self.art_manager.get_art(font_name, text)
        color = self.color_manager.get_color()
        width, height = self.size_manager.get_size()
        char = self.get_user_input("Введіть символ, який ви хочете використовувати (наприклад, '@','*'): ")

        colored_art = colored(art_object, color)
        print("Попередній перегляд вашого ASCII-арту:")
        formatted_art = colored_art.center(width).replace(' ', char)
        print(formatted_art)

        save_option = input("Зберегти ASCII-арт у файл? (так/ні): ").lower()
        if save_option == 'так':
            self.file_manager.save_art(formatted_art)

        print("Дякуємо за використання нашого генератора ASCII-арту!")

if __name__ == "__main__":
    generator = AsciiArtGenerator()
    generator.run()
