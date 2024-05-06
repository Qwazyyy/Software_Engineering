import json


def load_expenses(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses, filename):
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    description = input("Описание траты: ")
    amount = float(input("Введите сумму траты: "))
    expenses.append({"description": description, "amount": amount})


def display_expenses(expenses):
    print("Текущие траты:")
    for expense in expenses:
        print(f"Описание: {expense['description']}, Сумма: {expense['amount']}")


def main():
    filename = 'expenses.json'
    expenses = load_expenses(filename)

    while True:
        print("\n1. Добавить расход")
        print("2. Показать траты")
        print("3. Выйти из приложения")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses, filename)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            break
        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
