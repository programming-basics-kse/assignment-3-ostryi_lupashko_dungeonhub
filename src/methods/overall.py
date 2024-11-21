from typing import List

def get_country(my_country: str, info: dict) -> str:
    for key, value in info.items():
        if key in my_country:
            return key

        if my_country in key:
            info[my_country] = value
            del info[key]

        return my_country

def process_overall(countries: list[str]) -> str:

    with open('../../data/Olympics.tsv', 'r') as file:
        info = {}
        for line in file:
            row = line.strip().split('\t')
            country = get_country(row[6], info)
            year = row[9]

            if country in countries and row[14] != 'NA':
                if country not in info:
                    info[country] = {}
                if year not in info[country]:
                    info[country][year] = 0
                info[country][year] += 1

    if info == {}:
        return ""

    result = '\n\n'
    k = 1
    result += "================"
    result += '\n\n'
    for country in info:
        max = 0
        for year in range(1896, 1993, 4):
            try:
                if max < int(info[country][str(year)]):
                    max = int(info[country][str(year)])
                    maxyear = year
            except KeyError:
                continue

        for year in range(1992, 2016, 2):
            try:
                if max < int(info[country][str(year)]):
                    max = int(info[country][str(year)])
            except KeyError:
                continue

        result += f"{k}. {country}'s most medals year was: {maxyear}, {max} medals"

        result += '\n\n'
        result += "================"
        result += '\n\n'
        k += 1

    return result
