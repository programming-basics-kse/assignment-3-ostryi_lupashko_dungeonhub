import csv

if __name__ == '__main__':
    from utils import *
else:
    from .utils import *


def process_total(year):
    file_path = get_filepath("data/Olympics.tsv")

    with open(file_path, 'r') as file:
        info = {}
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        indexes = get_indexes(header)

        for row in reader:
            country = get_country(row[indexes["country"]], info)

            if row[indexes["year"]] == year and row[indexes["medal"]] != 'NA':
                if country not in info:
                    info[country] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                info[country][row[indexes["medal"]]] += 1

    result = ""

    for country in info:
        result += f"{country} - {info[country]['Gold']} - {info[country]['Silver']} - {info[country]['Bronze']}\n"

    return result

if __name__ == '__main__':
    print(process_total("2012"))
