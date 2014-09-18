import csv
from xlsx import Workbook

if __name__ == '__main__':
	users = {}
	societies = {}
	with open("users.csv") as f:
		reader = csv.reader(f);
		for row in reader:
			users[row[1]] = row[0]

	with open("societies.csv") as f:
		reader = csv.reader(f);
		for row in reader:
			societies[row[2].strip().upper()] = row[0]

	book = Workbook("Society Contacts.xlsx")
	join = open("join.txt", "w")
	snot_found = open("snot_found.txt", "w")
	unot_found = open("unot_found.txt", "w")

	for sheet in book:
		for row, cells in sheet.rows().iteritems():
			if len(cells) == 0:
				continue
			netid = cells[1].value
			society = cells[2].value.upper()
			if users.get(netid) and societies.get(society):
				join.write("(%s, %s, 0),\n" %(users[netid], societies[society]))
			else:
				if users.get(netid):
					snot_found.write(society + "\n")
				else:
					unot_found.write(netid + "\n")

		join.close()
		snot_found.close()
		unot_found.close()
		exit()
