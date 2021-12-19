with open('input.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		m=listl.append(strip_lines)


def get_first_line(input):
    first_line = []
    for item in input:
        if item == '':
            break
        first_line.append(item)

    return first_line

def parse_first_line(input):
    rest_list = input[0].split(',')
    return rest_list

def parse_rest(input):
    res = []
    input.pop(0)
    input.pop(0)
    tmp_list = []
    for item in input:
        if item == '':
            res.append(tmp_list)
            tmp_list= []
        else:
            tmp_list.append(item)
    res.append(tmp_list)  
    
    tmp_res = []
    for item in res:
        tmp_item = []
        for i in item:
            i = ' '.join(i.split())
            i = i.split(' ')
            tmp_item.append(i)
        tmp_res.append(tmp_item)
    
    
    return tmp_res


def is_winning(numbers, bingo):
    #print(numbers)
    for row in bingo:
        checker = 0
        for number in row:
            if number not in numbers:
                checker = 1
                break
        if checker == 0:
            
          #  print("Vitezna rada")
            return True

            
    length_of_bingo = len(bingo[0])
    
    for i in range(length_of_bingo):
        checker2 = 0
        for row in bingo:
            #print(row[i])
            if row[i] not in numbers:
                checker2 = 1
                break
        
        if checker2 == 0:
            print("Vitezny sloupec")
            return True


    return False

def play(numbers, bingos):
    numbers_played = []
    for number in numbers:
        numbers_played.append(number)
        for bingo in bingos:
            if is_winning(numbers_played, bingo) == True:
             #   print("Bingo {} vyhralo po tazeni cisel {}".format(bingo, numbers_played))
                return bingo, numbers_played

def calculate_result(bingo, numbers_played):
    sum = 0
    for row in bingo:
        for number in row:
            if number not in numbers_played:
                sum += int(number)
    return sum * int(numbers_played[-1])

def squid_win(numbers, bingos):
    numbers_played = []
    for number in numbers:
        numbers_played.append(number)
        for bingo in bingos:
            if is_winning(numbers_played, bingo) == True:
                print("Vyndam tady")
                bingos.remove(bingo)
            elif(len(bingos) == 1):
                result = bingos.copy()
                print("Copying result")
            elif(len(bingos) == 0):
                break
        if(len(bingos) == 0):
            break
          
    for item in result:
        result2 = item.copy()
        
    print(result2)
    print(numbers_played)
    return result2, numbers_played
     

first_line = get_first_line(listl)
first_line_parsed = parse_first_line(first_line)
bingos = parse_rest(listl)
bingo, numbers_played = squid_win(first_line_parsed, bingos)
result = calculate_result(bingo, numbers_played)
print(result)