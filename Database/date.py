with open("database", "a+") as file:
	current = []
	while True:
		name = input("Name: ")
		if name.upper() == "STOP":
			break
		else:
			if name in open("database").read():
				print("User is already in our database.")
			else: 
				if name not in current:
					file.write(name + '\n')
					current.append(name)
				else:
					print("User is already in our database.")


with open("database", "r") as file1:
	sortedd = []
	for line in file1:
		x = line.replace("\n", '')
		sortedd.append(x)

	sortedd2 = sorted(sortedd)
	
with open("sorted", 'w') as file2:
	for i in sortedd2:
		file2.write(i + '\n')