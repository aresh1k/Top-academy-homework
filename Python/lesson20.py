print("\nЗадание 1 - поменять местами две строки в файле")

text = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n"

with open("test1.txt", "w+") as file:
    file.write(text)
    file.seek(0)
    lines = file.readlines()
    print("\nЗначения до:", lines)
    lines[1], lines[2] = lines[2], lines[1]

with open("test1.txt", "w+") as file:
    file.writelines(lines)
    file.seek(0)
    print("\nЗначения после:", file.readlines())


print("\nЗадание 2 - изменить порядок список наоборот")

with open("test2.txt", "w+") as file:
    file.write(text)
    file.seek(0)
    lines = file.readlines()
    print("\nЗначения до:", lines)

with open("test2.txt", "w+") as file:
    file.writelines(lines[::-1])
    file.seek(0)
    print("\nЗначения после:", file.readlines())

print("\nЗадание 3 - объединить содержимое двух файлов в третьем")

with open("test1.txt", "r") as file1, open("test2.txt", "r") as file2, open("test3.txt", "w+") as file3:
    lines = file1.readlines() + file2.readlines()
    file3.writelines(lines)
    file3.seek(0)
    print("\nСодержимое нового файла:", file3.readlines())
