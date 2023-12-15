import math

memory = []

while True:
    try:
        # Запитуємо користувача про введення
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /, ^, sq, %): ")
        
        # Перевіряємо чи введений оператор є дійсним
        if operator not in ['+', '-', '*', '/', '^', 'sq', '%']:
            raise ValueError("Невідомий оператор")
        
        # Обробка операцій
        if operator == '+':
            num2 = float(input("Введіть друге число: "))
            result = num1 + num2
        elif operator == '-':
            num2 = float(input("Введіть друге число: "))
            result = num1 - num2
        elif operator == '*':
            num2 = float(input("Введіть друге число: "))
            result = num1 * num2
        elif operator == '/':
            num2 = float(input("Введіть друге число: "))
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе")
            result = num1 / num2
        elif operator == '^':
            num2 = float(input("Введіть показник степеня: "))
            result = num1 ** num2
        elif operator == 'sq':
            result = math.sqrt(num1)
        elif operator == '%':
            num2 = float(input("Введіть число для взяття залишку: "))
            result = num1 % num2
        
        # Додаємо результат до пам'яті
        memory.append(result)
        
        # Виводимо результат
        print(f"Результат: {result}")
        
        # Питаємо користувача, чи він хоче виконати ще одне обчислення
        another_calculation = input("Бажаєте виконати ще одне обчислення? (так/ні): ")
        if another_calculation.lower() != 'так':
            break
            
    except (ValueError, ZeroDivisionError) as error:
        print(f"Помилка: {error}")
    except Exception as error:
        print(f"Невідома помилка: {error}")

# Виводимо історію обчислень
print("Історія обчислень:")
for idx, item in enumerate(memory, start=1):
    print(f"{idx}: {item}")

