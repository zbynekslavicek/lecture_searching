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


def main():
    pass


if __name__ == '__main__':
    main()
    file = "sequential.json"
    field = "unordered_numbers"
    seq_data = read_data(file, field)
    print(seq_data)