class Calculator:
    def __init__(self):
        self.memory = []

    def get_user_input(self):
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, sq, %): ")
            if operator not in ['+', '-', '*', '/', '^', 'sq', '%']:
                raise ValueError("Невідомий оператор")
            num2 = float(input("Введіть друге число: "))
            return num1, num2, operator
        except (ValueError, ZeroDivisionError) as error:
            raise ValueError(f"Помилка: {error}")

    def perform_calculation(self, num1, num2, operator):
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль неможливе")
                result = num1 / num2
            elif operator == '^':
                result = num1 ** num2
            elif operator == 'sq':
                result = num1 ** (1 / num2)
            elif operator == '%':
                result = num1 % num2
            else:
                raise ValueError("Невідомий оператор")
            self.memory.append(result)
            print(f"Результат: {result}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"Помилка: {error}")

    def run_calculator(self):
        while True:
            try:
                num1, num2, operator = self.get_user_input()
                self.perform_calculation(num1, num2, operator)
            except ValueError as error:
                print(f"Помилка: {error}")
            finally:
                another_calculation = input("Бажаєте виконати ще одне обчислення? (так/ні): ")
                if another_calculation.lower() != 'так':
                    self.show_calculation_history()
                    break

    def show_calculation_history(self):
        print("Історія обчислень:")
        for idx, item in enumerate(self.memory, start=1):
            print(f"{idx}: {item}")

# Створюємо екземпляр класу Calculator та викликаємо метод run_calculator()
calc = Calculator()
calc.run_calculator()

