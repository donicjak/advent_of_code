with open('input.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		m=listl.append(strip_lines)

print(listl)
horizontal = 0
depth = 0
for i in listl:
    command, number = i.split(' ')
    if( command == 'forward'):
        horizontal += int(number)
    elif(command == 'down'):
        depth += int(number)
    else:
        depth -= int(number)

print("Horizontal is {} and depth is {}".format(horizontal, depth))