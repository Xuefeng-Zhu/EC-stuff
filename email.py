if __name__ == '__main__':
	f = open("ec-committees.txt")
	o = open("ec-email.txt", "w")
	for i in f:
		email = i.strip('\n')
		if email:
			o.write("%s@illinois.edu\n" %email)