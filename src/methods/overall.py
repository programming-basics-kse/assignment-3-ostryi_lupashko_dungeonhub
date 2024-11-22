import csv
from utils import *


def process_overall(countries: list[str]) -> str:
    file_path = get_filepath("data/Olympics.tsv")

    with open(file_path, 'r') as file:
        info = {}
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        set_indexes(header)

        for row in reader:
            country = get_country(row[country_index], info)
            year = row[year_index]

            if country in countries and row[medal_index] != 'NA':
                if country not in info:
                    info[country] = {}
                if year not in info[country]:
                    info[country][year] = 0
                info[country][year] += 1

    if info == {}:
        return ""

    k = 1

    result = ""

    for country in info:
        max = 0

        for year in info[country]:
            if max < int(info[country][str(year)]):
                max = int(info[country][str(year)])
                maxyear = year

        result += f"{k}. {country}'s most medals year was: {maxyear}, {max} medals"

        k += 1

    return result
