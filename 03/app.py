with open('input.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		m=listl.append(strip_lines)

print(listl)
print(len(listl[0]))

gamma = ""
for i in range(len(listl[0])):
    counter_zero = 0
    counter_one = 0
    for item in listl:
        if item[i] == '0':
            counter_zero += 1
        else:
            counter_one += 1
        
        if item == listl[-1]:
            if counter_zero > counter_one:
                gamma += '0'
            else:
                gamma += '1'

print(gamma)
epsilon = ""
for char in gamma:
    if(char == '0'):
        epsilon += '1'
    else:
        epsilon += '0'
print(epsilon)

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)
print(gamma_dec)
print(epsilon_dec)
print("Vysledek je {}".format(gamma_dec*epsilon_dec))