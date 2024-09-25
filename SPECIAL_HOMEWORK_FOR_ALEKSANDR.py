def read_students(file_name):
    students = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            name, grade = line.strip().split()
            students[name.lower()] = grade
    return students


def main():
    students = read_students('students.txt')
    for names in students.keys():
        print(f'Имя студента: {names}')
    name_to_search = input("Введите имя студента для поиска оценки: ").lower()

    if name_to_search in students:
        print(f"Оценка {name_to_search}: {students[name_to_search]}")
    else:
        print(f"Студент с именем {name_to_search} не найден")


if __name__ == "__main__":
    main()
