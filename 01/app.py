import time

with open('input.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		m=listl.append(strip_lines)

counter = 0
for i in range(len(listl)):
    if( i == 0):
        continue
    elif(listl[i] > listl[i-1]):
        print("Increased")
        counter += 1
    else:
        print("Decreased")

print("Vyslo nam zde {}".format(counter))