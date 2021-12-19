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

input_text = get_input('input.txt')
parsed_input = parse_input(input_text)
total_cost = find_crab(parsed_input)
print(total_cost)
