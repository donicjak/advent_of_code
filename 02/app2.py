with open('input.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		m=listl.append(strip_lines)

print(listl)
horizontal = 0
depth = 0
aim = 0
for i in listl:
    command, number = i.split(' ')
    if( command == 'forward'):
        horizontal += int(number)
        depth += aim * int(number)
    elif(command == 'down'):
        aim += int(number)
    else:
        aim -= int(number)

print("Horizontal is {} and depth is {} and aim is {}".format(horizontal, depth, aim))
print(f'final result is {horizontal*depth}')