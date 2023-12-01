
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content

def process_input(input):
    data = input.splitlines()
    return data


def calc_part_one(data):
    first = False
    last = False

    sum = 0

    for row in data:
        for char in row:
            try:
                if not first:
                    first = int(char)
                    last = int(char)
                else:
                    last = int(char)
            except:
                pass
        sum += (int(str(first) + str(last)))
        first = False;
    
    return sum



def calc_part_two(data):
    letter_to_int = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine"
    }

    first = False
    last = False

    sum = 0

    for row in data:
        new_row = row
        for k, v in letter_to_int.items():
            new_row = new_row.replace(k, str(v))
        for char in new_row:
            try:
                if not first:
                    first = int(char)
                    last = int(char)
                else:
                    last = int(char)
            except:
                pass
        sum += (int(str(first) + str(last)))
        first = False;
    return sum



def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)


    print("Part one: {}\nPart two: {}".format(part_one, part_two))



if __name__ == "__main__":
    main()