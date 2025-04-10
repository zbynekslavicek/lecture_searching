import os
import json
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

    allowed_fields = {"unordered_numbers", "ordered_numbers", "dna_sequence"}
    if field not in allowed_fields:
        return None

    with open(file_path, "r") as file:
        data = json.load(file)

    return data[field]


def linear_search(sekvence, hledane_cislo):
    konecny_slovnik = {}



def main():
    pass


if __name__ == '__main__':
    main()
    numbers = read_data("sequential.json", field="unordered_numbers")
    print(numbers)