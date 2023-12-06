import pandas as pd


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = ([[int(x) for x in value.split(':')[1].strip().split(' ') if x != ''] for value in input.splitlines()])
    return data

 
def calc_part_one(data):
    values = 1
    
    for time, distance in zip(data[0], data[1]):
        df = pd.DataFrame({'ms': range(time+1)})

        df['speed'] = df['ms']
        df['time_left'] = time - df['ms']
        df['distance'] = df['speed'] * df['time_left']
        df['winning'] = df['distance'] > distance

        values *= df['winning'].sum()

    return values


def calc_part_two(data):

    time = int(''.join(map(str, data[0])))
    distance = int(''.join(map(str, data[1])))
        
    df = pd.DataFrame({'ms': range(time+1)})

    df['speed'] = df['ms']
    df['time_left'] = time - df['ms']
    df['distance'] = df['speed'] * df['time_left']
    df['winning'] = df['distance'] > distance

    return df['winning'].sum()


def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()