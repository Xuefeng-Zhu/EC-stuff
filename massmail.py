if __name__ == '__main__':
	f = open("massmail.txt")
	for i in f:
		email = i.strip('\n')
		if email:
			print "%s \\" %email