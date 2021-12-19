from collections import Counter

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
    return result

def iterating_over_fish(fishes):
    timers = Counter({timer: 0 for timer in range(10)})
    fishes = Counter(fishes)
    fishes.update(timers)
    
    for day in range(256):
        fishes[7] += fishes.get(0, 0)
        fishes[9] += fishes.get(0, 0)
        fishes = {fish: fishes.get(fish + 1, 0) for fish in fishes}
        
    return sum(fishes.values())

    
input_text = get_input("input.txt")
parsed_input = parse_input(input_text)
result = iterating_over_fish(parsed_input)
print(result)