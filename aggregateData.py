import csv
def aggregate_data():
    file = open('all_dota_data.csv', 'a')
    writer = csv.writer(file)
    writer.writerow(['PATCH', 'CATEGORY', 'ORDINAL RANK', 'PERCENT VALUE', 'HERO NAME'])
    for i in range(1, 5):
        csv_file = open('dota_data_' + str(i) + '.csv', 'r')
        reader = csv.reader(csv_file)
        for line in reader:
            writer.writerow(line)
    file.close()
