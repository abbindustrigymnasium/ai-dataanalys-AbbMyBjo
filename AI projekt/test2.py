import csv

with open('AI_values.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([2, 2, 2])
    print('skriver till excel')

