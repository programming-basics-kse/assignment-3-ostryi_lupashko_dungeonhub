import csv
from utils import *


def process_total(year):
    file_path = get_filepath("data/Olympics.tsv")

    with open(file_path, 'r') as file:
        info = {}
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        set_indexes(header)

        for row in reader:
            country = get_country(row[country_index], info)

            if row[year_index] == year and row[medal_index] != 'NA':
                if country not in info:
                    info[country] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                info[country][row[medal_index]] += 1

    if info == {}:
        return ""

    result = ""
    for country in info:
        result += f"{country} - {info[country]['Gold']} - {info[country]['Silver']} - {info[country]['Bronze']}"
        result += "\n\n"

    return result
