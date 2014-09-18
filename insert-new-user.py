from xlsx import Workbook

if __name__ == '__main__':
	book = Workbook("Society Contacts.xlsx")
	users = {}
	for sheet in book:
		for row, cells in sheet.rows().iteritems():
			if len(cells) == 0 or len(cells[0].value) == 0:
				continue
			full_name = cells[0].value.split()
			first_name = " ".join(full_name[:-1])
			last_name = full_name[-1]
			netid = cells[1].value
			users[netid] = "(NULL, '%s', '%s', '%s', NULL)" %(netid, first_name, last_name)

	new_users = open("new_users.txt", "w")
	with open("unot_found.txt") as f:
		for user in f:
			new_users.write(users[user.strip("\n")] + ",\n")
	new_users.close()

