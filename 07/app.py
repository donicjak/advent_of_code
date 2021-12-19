def get_input(input):
    with open(input,'r') as f:
        listl=[]
        for line in f:
            strip_lines=line.strip()
            m=listl.append(strip_lines)
    return listl

def parse_input(input):
    res = []
    tmp_word = ""
    for item in input:
        for i in range(len(item)):
            if item[i] != ',':
                tmp_word += str(item[i])
            else:
                res.append(int(tmp_word))
                tmp_word = ""
        res.append(int(tmp_word))

    return res


def find_crab(crabs):
    max_number = float('inf')
    for crab in crabs:
        number = 0
        for crab2 in crabs:
            if crab2 > crab:
                number += crab2 - crab
            else:
                number += crab - crab2
        if number < max_number:
            max_number = number
    return max_number

def count_fuel(crab1, crab2):
    #print(f'crab1 je {crab1} a crab2 je {crab2}')
    number = 0
    row_of_numbers = []
    while crab1 != crab2:
        crab1 += 1
        row_of_numbers.append(crab1)
    #print(f'row of numbers je {row_of_numbers}')
    for index, item in enumerate(row_of_numbers):
        number += 1 + index
    #print(f'number je {number}')
    return number
def find_crab2(crabs):
    max_number = float('inf')
    winning_crab = []
    all_crabs = [i for i in range(min(crabs), max(crabs)+1)]
    print(f'max value je {max(crabs)+1}')
    #print(f'All crabs is {all_crabs}')
    for crab in all_crabs:
        print(f'Aktualni crab je {crab}')
        number = 0
        for crab2 in crabs:
            if crab2 > crab:
                number += count_fuel(crab, crab2)
            else:
                number += count_fuel(crab2, crab)
        if number < max_number:
            max_number = number
            winning_crab = crab
    print(f'Winning crab is {winning_crab}')
    return max_number

input_text = get_input('input.txt')
parsed_input = parse_input(input_text)
total_cost = find_crab(parsed_input)
total_cost2 = find_crab2(parsed_input)
print(total_cost2)
