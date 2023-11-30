import pandas as pd

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content

def process_input(input):
    data = pd.DataFrame([input.splitlines()])
    return data.T.astype(int)

def main():
    test_input = read_file('test_input.txt')
    test_data = process_input(test_input)
    test_answer = 6
    
    part_one = test_data.sum()[0]
    
    assert part_one == test_answer


    part_one = 0 
    part_two = 0

    print("Part one: {}\nPart two: {}".format(part_one, part_two))



if __name__ == "__main__":
    main()