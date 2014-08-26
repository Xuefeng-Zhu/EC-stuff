# generate lists of email for massmail 

if __name__ == '__main__':
	f = open("massmail.txt")
	count = 1
	list_email = []
	for i in f:
		email = i.strip('\n')
		if email:
			list_email.append("%s \\\n" %email)
			if (len(list_email) == 3000):
				f = open("list%d.txt" %count, "w")
				f.writelines(list_email)
				list_email = []
				count += 1
	f = open("list%d.txt" %count, "w")
	f.writelines(list_email)
