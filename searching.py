import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as f:
        allowed_key = json.load(f)

    if field not in allowed_key:
        return None

    with open(file_name, "r") as f:
        data = json.load(f)

    return data[field]


def linear_search(sequence, cislo):
    pozice = []
    count = 0

    for i, num in enumerate(sequence):
        if num == cislo:
            pozice.append(i)
            count += 1

    return {"positions": pozice, "count": count}


def pattern_search(sequence, patern):
    pozice = set()
    delka_paternu = len(patern)
    delka_sequence = len(sequence)

    i = 0
    while i <= delka_sequence - delka_paternu:
        j = 0
        while j < delka_paternu and sequence[i + j] == patern[j]:
            j += 1
        if j == delka_paternu:
            pozice.add(i)
            i += 1
        else:
            i += max(1, j)

    return pozice

def main():
    pass


if __name__ == '__main__':
    main()
    file = "sequential.json"
    field = "unordered_numbers"
    seq_data = read_data(file, field)
    print(seq_data)

    cislo = 63
    result = linear_search(file, cislo)

    print(f"Positions: {result['positions']}")
    print(f"Count: {result['count']}")