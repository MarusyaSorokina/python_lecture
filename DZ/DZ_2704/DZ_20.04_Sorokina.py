test = "test.txt"
with open(test, "w") as f:
    f.write("Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл;\n")

with open(test, "r") as f:
    lines = f.readlines()
    print("Исходные строки: ")
    for i, line in enumerate(lines):
        print(f"{i}: {line.strip()}")

    try:

        pos1 = int(input("Какую строку заменить: "))
        pos2 = int(input("На какую строку заменить: "))

        if 0 <= pos1 < len(lines) and 0 <= pos2 < len(lines):

            lines[pos1], lines[pos2] = lines[pos2], lines[pos1]      # меняем строки местами

            with open(test, "w") as f:                                 # записываем обратно файл
                f.writelines(lines)

            print("Строки заменены. Обновленный файл:")
            for i, line in enumerate(lines):
                print(f"{i}:{line.strip()}")

        else:
            print("Ошибка. Введены некорректные значения.")

    except ValueError:
        print("Ошибка. Введите целые числа.")











