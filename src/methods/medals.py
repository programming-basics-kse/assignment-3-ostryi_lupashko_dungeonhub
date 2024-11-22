import csv
from utils import *


def process_medals(country: str, year: str):
    file_path = get_filepath("data/Olympics.tsv")

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        info = []
        set_indexes(header)
        k = 0

        for row in reader:
            if country in row[country_index] and row[year_index] == year and row[medal_index] != 'NA':
                sportsman = {'Name': row[name_index], "Sport": row[sport_index], "Medal": row[medal_index]}
                info.append(sportsman)
                k += 1
                if k == 10:
                    break

    result = ""
    if not info:
        return ""

    k = 1
    for i in range(0, len(info)):
        result += f"{k}. Name: {info[i]['Name']},\n"
        result += f"Sport: {info[i]['Sport']},\n"
        result += f"Medal: {info[i]['Medal']}.\n\n"
        result += '=======================\n\n'
        k += 1

    return result
