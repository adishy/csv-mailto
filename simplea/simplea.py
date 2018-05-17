import csv

try:
	somefile = open('cnaj.csv', 'r')

	read_csv_provided = csv.reader(somefile)

	for some_row in read_csv_provided:
		for a in some_row:
			print(a);

except FileNotFoundError:
	print("File not found in specified path");