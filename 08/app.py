def get_input(input):
    with open(input,'r') as f:
        listl=[]
        for line in f:
            strip_lines=line.strip()
            m=listl.append(strip_lines)
    return listl

def parse_input(input):
    res = []
    for item in input:
        item_l = []
        digit = ""
        for i in range(len(item)):
            if item[i] != ' ':
                digit += item[i]
            else:
                item_l.append(digit)
                digit = ""
        item_l.append(digit)
        res.append(item_l)
    return res

def find_unique_numbers(digits):
    res = 0
    for line in digits:
        flag_delimiter = False
        for digit in line:
            if digit == '|':
                flag_delimiter = True
            elif flag_delimiter == True:
                if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                    res += 1

    return res



input_raw = get_input('input.txt')
parsed_input = parse_input(input_raw)
unique_numbers = find_unique_numbers(parsed_input)
print(unique_numbers)
