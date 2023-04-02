import csv

with open("data2.csv", "r") as f:
    file_reader = csv.reader(f, delimiter=";")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы: {','.join(row)}")
        else:
            print(f"hostname - {row[0]}; vendor - {row[1]}; model - {row[2]}; location - {row[3]}")
        count += 1
