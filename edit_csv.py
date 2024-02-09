import csv
from sys import argv

with open('data.csv', 'a', newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow([argv[1],argv[2],argv[3]])