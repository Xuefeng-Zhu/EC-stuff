if __name__ == '__main__':
	f = open("ec-committees.txt")
	for i in f:
		line = i.strip('\n')
		if line:
			print line