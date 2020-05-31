import csv
# keep here for now, but also keep copy in main, while developing, decide where to have this function
def read_csv_file(file_name):
    with open(file_name, newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=",")
        for row in filereader:
            print(', '.join(row))


read_csv_file('package-data.csv')