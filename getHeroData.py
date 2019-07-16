import csv
def get_hero_data(hero_name):
    read_file = open('all_dota_data.csv', 'r')
    reader = csv.reader(read_file)
    
    write_file = open(hero_name+'.csv', 'a')
    writer = csv.writer(write_file)
    
    writer.writerow([hero_name+' STATS', '|'])
    writer.writerow(['PATCH', 'CATEGORY', 'ORDINAL RANK', 'PERCENT VALUE'])
    
    try:
        for line in reader:
            if line[4] == hero_name:
                writer.writerow(line[:4])
    except IndexError:
        pass
            
    read_file.close()
    write_file.close()
