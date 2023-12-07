import pandas as pd


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except Exception as e:
        print("Something went wrong: ", e)

    return content


def process_input(input):
    data = pd.DataFrame([[list(x) for x in row.split(' ')][0] for row in input.splitlines()])
    data["bid"] = [row.split(' ')[1] for row in input.splitlines()]
    
    return data

 
def calc_part_one(data):

    label_to_num = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }

    quality_of_hand = {
        '5': 7,
        '41': 6,
        '32': 5,
        '311': 4,
        '221': 3,
        '2111': 2,
        '11111': 1,
    }

    data = data.apply(lambda x: x.map(label_to_num).fillna(x)).astype(int)
    data['type'] = data.apply(lambda x: quality_of_hand[''.join(x.iloc[:5].value_counts().values.astype(str))], axis=1)
    data['sort_val'] = data.apply(lambda row: int(
            str(row['type']) + 
            str(row[0]).zfill(2) + 
            str(row[1]).zfill(2) +  
            str(row[2]).zfill(2) + 
            str(row[3]).zfill(2) + 
            str(row[4]).zfill(2))
        , axis=1)
    
    data_sorted = data.sort_values("sort_val")
    data_sorted["rank"] = range(1, len(data_sorted)+1)

    data_sorted["winnings"] = data_sorted["rank"] * data_sorted["bid"]
    return data_sorted["winnings"].sum()


def calc_part_two(data):
    label_to_num = {
        'T': 10,
        'J': 1,
        'Q': 12,
        'K': 13,
        'A': 14,
    }

    data = data.apply(lambda x: x.map(label_to_num).fillna(x)).astype(int)

    quality_of_hand = {
        '5': 7,
        '41': 6,
        '32': 5,
        '311': 4,
        '221': 3,
        '2111': 2,
        '11111': 1,
    }

    data['type'] = data.apply(lambda x: quality_of_hand[''.join(x.iloc[:5].value_counts().values.astype(str))], axis=1)
    data['jokers'] = data[data.iloc[:,0:5] == 1].count(axis=1)

    def promote(times, old_type):
        if times == 5: return 7
        if times == 4: return 7
        if times == 3: return old_type+2
        if times == 2: return min(old_type*2, 7)
        if times == 1: 
            jack_promotion = {
                6: 7,
                4: 6,
                3: 5,
                2: 4,
                1: 2,
            }
            return jack_promotion[old_type]
        return old_type

    data['type'] = data.apply(lambda x: promote(x['jokers'], x['type']), axis=1) 
    data['sort_val'] = data.apply(lambda row: int(
            str(row['type']) + 
            str(row[0]).zfill(2) + 
            str(row[1]).zfill(2) +  
            str(row[2]).zfill(2) + 
            str(row[3]).zfill(2) + 
            str(row[4]).zfill(2))
        , axis=1)
    
    data_sorted = data.sort_values("sort_val")
    data_sorted["rank"] = range(1, len(data_sorted)+1)

    data_sorted["winnings"] = data_sorted["rank"] * data_sorted["bid"]
    return data_sorted["winnings"].sum()



def main():
    input = read_file('input.txt')
    data = process_input(input)

    part_one = calc_part_one(data)
    part_two = calc_part_two(data)

    print("Part one: {}\nPart two: {}".format(part_one, part_two))


if __name__ == "__main__":
    main()