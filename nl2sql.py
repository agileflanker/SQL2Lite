import csv

def printNL2SQLresult():
    file = "nl2sql_results.csv"

    with open(file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)

        next(reader)

        for row in reader:
            print(f"{row[0]},\"{row[1]}\",{row[2]},\"{row[3]}\",{row[4]},\"{row[5]}\",{row[6]},{row[7]},{row[8]},{row[9]},{row[10]}")
