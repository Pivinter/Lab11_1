def add_term(terms_list, term, explanation):
    terms_list.append({"term": term, "explanation": explanation})


def remove_term(terms_list, term):
    for item in terms_list:
        if item["term"] == term:
            terms_list.remove(item)
            break


def display_terms(terms_list):
    for item in terms_list:
        print(f"{item['term']}:\n{item['explanation']}\n")


def sort_terms(terms_list):
    return sorted(terms_list, key=lambda x: x["term"])


def find_term(terms_list, term):
    for item in terms_list:
        if item["term"] == term:
            return item["explanation"]
    return None


def save_to_file(terms_list, filename):
    with open(filename, "w") as file:
        for item in terms_list:
            file.write(f"{item['term']}|{item['explanation']}\n")


def load_from_file(filename):
    terms_list = []
    with open(filename, "r") as file:
        for line in file:
            term, explanation = line.strip().split("|")
            terms_list.append({"term": term, "explanation": explanation})
    return terms_list

def user_input(prompt, error_message, validation_function):
    while True:
        user_input = input(prompt)
        if validation_function(user_input):
            return user_input
        else:
            print(error_message)

def validate_menu_choice(choice):
        return choice.isdigit() and 1 <= int(choice) <= 8

def validate_filename(filename):
    return len(filename) > 0

def main():
    terms_list = []
    while True:
        print("\nМеню:")
        print("1. Додати термін")
        print("2. Вилучити термін")
        print("3. Переглянути терміни")
        print("4. Знайти термін")
        print("5. Зберегти у файл")
        print("6. Завантажити з файлу")
        print("7. Сортувати терміни")
        print("8. Вийти з програми")

        choice = user_input("Введіть число від 1 до 8: ", "Неправильний вибір. Спробуйте ще раз.", validate_menu_choice)

        if choice == "1":
            term = input("Введіть термін: ")
            explanation = input("Введіть пояснення: ")
            add_term(terms_list, term, explanation)
        elif choice == "2":
            term = input("Введіть термін для вилучення: ")
            remove_term(terms_list, term)
        elif choice == "3":
            display_terms(terms_list)
        elif choice == "4":
            term = input("Введіть термін для пошуку: ")
            explanation = find_term(terms_list, term)
            if explanation:
                print(f"{term}:\n{explanation}\n")
            else:
                print("Термін не знайдено.")
        elif choice == "5":
            filename = user_input("Введіть ім'я файлу для збереження: ", "Неправильне ім'я файлу. Спробуйте ще раз.", validate_filename)
            save_to_file(terms_list, filename)
        elif choice == "6":
            filename = user_input("Введіть ім'я файлу для завантаження: ", "Неправильне ім'я файлу. Спробуйте ще раз.", validate_filename)
            try:
                terms_list = load_from_file(filename)
            except FileNotFoundError:
                print("Файл не знайдено.")
        elif choice == "7":
            terms_list = sort_terms(terms_list)
        else:
            break

if __name__ == "__main__":
    main()