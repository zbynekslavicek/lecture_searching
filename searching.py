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
    konecny_slovnik = []

    for index, value in enumerate(sekvence):
        if value == hledane_cislo:
            konecny_slovnik.append(index)
        else:
            return sekvence

    vysledek = {
        "positions": pozice,
        "count": len(pozice)
    }
    return vysledek




def main():
    pass

def pattern_search(sekvence, vzor):

    pozice_nalezu = set()
    delka_vzoru = len(vzor)
    max_index = len(sekvence) - delka_vzoru + 1

    for i in range(max_index):
        shoda = True
        for j in range(delka_vzoru):
            if sekvence[i + j] != vzor[j]:
                shoda = False
                break
        if shoda:
            pozice_nalezu.add(i)

    return pozice_nalezu

def binary_search(seznam, hledane_cislo):

    left = 0
    right = len(seznam) - 1

    while left <= right:
        mid = (left + right) // 2
        if seznam[mid] == hledane_cislo:
            return mid
        elif seznam[mid] < hledane_cislo:
            left = mid + 1
        else:
            right = mid - 1

    return None


if __name__ == '__main__':
    main()
    numbers = read_data("sequential.json", field="unordered_numbers")
    print(numbers)
    hledane_cislo = 5
    vysledek_vyhledavani = linear_search([54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5], hledane_cislo)
    print(f"Výsledek vyhledávání čísla {hledane_cislo}:", vysledek_vyhledavani)
    vzor = "ATA"
    vysledek = pattern_search("ATGACGGAATATAAGCTAGGTGGTGGCTGGGCAGTCCGCGCTGATAGGGCAAGAGTGCGCGTACCATACCACGCTAAGCCATATAGGGCATCAGTCAGCCTGGCA", vzor)
    print(f"Vzor '{vzor}' nalezen na pozicích:", vysledek)

    cislo = 5
    vysledek_vyh = linear_search(
        [54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5],
        cislo)
    print(vysledek_vyh)