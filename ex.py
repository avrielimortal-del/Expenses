def add_expenses():
    category = input("Введите категорию расхода: ")
    try:
        amount = float(input("Введите сумму расходов: "))
    except ValueError:
        print("Ошибка! Сумма должна быть числом")
        return
    with open("expenses.txt", "a", encoding="utf-8") as f:
        f.write(f"{category}: {amount}\n")

def view_expenses():
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            expenses = f.readlines()
    except FileNotFoundError:
        print("Расходов пока нет!")
        return
    if not expenses:
        print("Расходов нет!")
        return
    print("Ваши расходы:")
    for index, line in enumerate(expenses, 1):
        parts = line.strip().split(":")
        if len(parts) == 2:
            category, amount = parts
            print(f"{index}. {category.strip()} — {amount.strip()}")

def del_expenses():
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            ex = f.readlines()
    except FileNotFoundError:
        print("Расходов пока нет!")
        return
    if not ex:
        print("Расходов нет!")
        return
    print("Ваши расходы:")
    for index, note in enumerate(ex, 1):
        print(f"{index}. {note.strip()}")
    try:
        ex_to_delete = int(input("Введите номер для удаления: "))
    except ValueError:
        print("Ошибка! Введите число.")
        return
    if 1 <= ex_to_delete <= len(ex):
        del ex[ex_to_delete - 1]
        with open("expenses.txt", "w", encoding="utf-8") as f:
            f.writelines(ex)
        print("Заметка удалена успешно!")
    else:
        print("Ошибка! Заметки с таким номером нет")

def total_expenses():
    total_sum = 0
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            for line in f:
                try:
                    parts = line.split(":")
                    amount = float(parts[1].strip())
                    total_sum += amount
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        print("Расходов пока нет!")
        return
    print(f"Общая сумма расходов: {round(total_sum, 2)}")

while True:
    print("\n1. Добавить расход")
    print("2. Показать расходы")
    print("3. Удалить заметку")
    print("4. Посчитать все расходы")
    print("5. Выход")
    x = input("Выбери действие: ")
    if x == "1":
        add_expenses()
    elif x == "2":
        view_expenses()
    elif x == "3":
        del_expenses()
    elif x == "4":
        total_expenses()
    elif x == "5":
        print("Хорошего дня!")
        break
    else:
        print("Ошибка! Такого действия нет.")