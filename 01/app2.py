import time

with open('input.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		m=listl.append(strip_lines)

counter = 0
for i in range(len(listl)):
    if i > len(listl)-4 :
        break
    else:
        sum1 = int(listl[i]) + int(listl[i+1]) + int(listl[i+2])
        sum2 = int(listl[i+1]) + int(listl[i+2]) + int(listl[i+3])
        print(sum1, sum2)
        if(sum1 < sum2):
            counter += 1

print("Vyslo nam zde {}".format(counter))