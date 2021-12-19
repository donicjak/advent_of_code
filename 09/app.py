import numpy as np

def get_input(input):
    with open(input,'r') as f:
        listl=[]
        for line in f:
            strip_lines=line.strip()
            m=listl.append(strip_lines)
    return listl

def parse_input(input):
    result = []
    for item in input:
        tmp_list = []
        for i in range(len(item)):
            tmp_list.append(item[i])
        result.append(tmp_list)
    return result

def make_2d_array(parsed_input):
    a = np.array(parsed_input)
    return a

def find_in_raws(locations):
    results = []
    j = 0
    for location in locations:
        #print(f'{location} and we are in row {j}')
        for i in range(len(location)):
            if j == 0:
                #print("Jsme na zacatku")
                if i == 0:
                    if location[i] < location[i+1] and location[i] < locations[j+1][i]:
                        #print(f'{location[i]} is at the beginning of the location and is smaller than {location[i+1]} and smaller than {location[i][j+1]}.')
                        results.append(location[i])
                elif i == len(location) - 1:
                    if location[i] < location[i-1] and location[i] < locations[j+1][i] :
                        #print(f'{location[i]} is at the end of the location and is smaller than {location[i-1]} and than {locations[j+1][i]}.')
                        results.append(location[i])

                else:
                    if location[i] < location[i+1] and location[i] < location[i-1] and location[i] < locations[j+1][i]:
                        #print(f'{location[i]} is in the middle and is smaller than {location[i+1]} and than {location[i-1]}.')
                        results.append(location[i])
            elif j == len(locations) - 1:
            #    print("Jsme na konci")
                if i == 0:
                    if location[i] < location[i+1] and location[i] < locations[j-1][i]:
                    #    print(f'{location[i]} is at the beginning of the location and is smaller than {location[i+1]} and smaller than {location[i][j-1]}.')
                        results.append(location[i])
                elif i == len(location) - 1:
                    if location[i] < location[i-1] and location[i] < locations[j-1][i] :
                        #print(f'{location[i]} is at the end of the location and is smaller than {location[i-1]} and than {locations[j-1][i]}.')
                        results.append(location[i])
                else:
                    if location[i] < location[i+1] and location[i] < location[i-1] and location[i] < locations[j-1][i]:
                    #    print(f'{location[i]} is in the middle and is smaller than {location[i+1]} and than {location[i-1]}.')
                        results.append(location[i])
            else:
            #    print("Jsme uprosted")
                if i == 0:
                    #print("i je 0")
                #  #  print(f"prvni je {location[i+1]} druhy je {locations[j-1][i]} a treti je {locations[j+1][i]} ")
                    if location[i] < location[i+1] and location[i] < locations[j-1][i] and location[i] < locations[j+1][i]:
                        #print(f'{location[i]} is at the beginning of the location and is smaller than {location[i+1]} and smaller than  and {locations[j-1][i]} and {locations[j+1][i]}.')
                        results.append(location[i])
                elif i == len(location) - 1:
                    if location[i] < location[i-1] and location[i] < locations[j-1][i] and location[i] < locations[j+1][i]:
                        #print(f'{location[i]} is at the end of the location and is smaller than {location[i-1]} and than {locations[j-1][i]}  and {locations[j-1][i]} and {locations[j+1][i]}.')
                        results.append(location[i])
                else:
                    if location[i] < location[i+1] and location[i] < location[i-1] and location[i] < locations[j-1][i] and location[i] < locations[j+1][i]:
                        #print(f'{location[i]} is in the middle and is smaller than {location[i+1]} and than {location[i-1]} and {locations[j-1][i]} and {locations[j+1][i]}.')
                        results.append(location[i])
        j += 1
    return results



def get_result(locations):
    sum = 0
    for location in locations:
        sum += int(location) + 1
    return sum

def find_basin(locations_basin):
    print(locations_basin)
    correct_locations = find_in_raws(locations_basin)
    print(correct_locations)

input_raw = get_input('input.txt')
parsed_input = parse_input(input_raw)
array2d = make_2d_array(parsed_input)
correct_locations = find_in_raws(array2d)
result = get_result(correct_locations)
print(result)
basins = find_basin(array2d)
