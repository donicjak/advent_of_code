import numpy as np

def get_input(input):
    with open(input,'r') as f:
        listl=[]
        for line in f:
            strip_lines=line.strip()
            m=listl.append(strip_lines)
    return listl

def parse_input(input_text):
    for item in input_text:
        item = item.replace(',', '')
        result = [int(char) for char in item]
    my_array = np.array(result)
    return my_array

def iterating_over_fish(parsed):
    tmp_parsed = np.array(parsed)
    for i in range(4):
        print("-----------------------------------")
        print(f"i je: {i}")
        print(parsed)
        # parsed = np.array(tmp_parsed)
        with np.nditer(parsed, op_flags=['readwrite']) as it:
            for x in it:
                print(x)
                if x == 0:
                    x[...] = 6
                    tmp_parsed = np.array(parsed)
                    tmp_parsed = np.append(tmp_parsed, 8)
                    
                else:
                    x[...] = x - 1
            
            
        print(tmp_parsed)
            


            
            
input_text = get_input("input.txt")
parsed_input = parse_input(input_text)
result = iterating_over_fish(parsed_input)