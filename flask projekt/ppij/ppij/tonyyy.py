import csv

def istina():
    with open ("/Users/danicavladic/Desktop/tony.csv") as tony:
        reader = csv.reader(tony, delimiter=';')
        i = 0
        for row in reader:
            if i == 0:
                return row[0]
            i += 1



