import csv

if __name__ == '__main__':
    from utils import *
else:
    from .utils import *


def process_overall(countries: list[str]) -> str:
    file_path = get_filepath("data/Olympics.tsv")

    with open(file_path, 'r') as file:
        info = {}
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        indexes = get_indexes(header)

        for row in reader:
            country = get_country(row[indexes["country"]], info)
            year = row[indexes["year"]]

            if country in countries and row[indexes["medal"]] != 'NA':
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

        result += f"{k}. {country}'s most medals year was: {maxyear}, {max} medals\n"

        k += 1

    return result

if __name__ == '__main__':
    print(process_overall(["United States", "Ukraine", "Georgia"]))