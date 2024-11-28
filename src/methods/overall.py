import csv

if __name__ == '__main__':
    from utils import *
    from row import Row
else:
    from .utils import *
    from .row import Row

def get_medals_data(inputFile, countries: list[str]):
    info = {}

    with open(get_filepath(inputFile), 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        indexes = get_indexes(header)

        for line in reader:
            row = Row(line, indexes)

            country = get_country(row.get_country(), info)  # Instead of doing this we can just repair dataset

            if country in countries and row.has_medal():
                if country not in info:
                    info[country] = {}

                if row.get_year() not in info[country]:
                    info[country][row.get_year()] = 0

                info[country][row.get_year()] += 1

    return info

def process_overall(inputFile, countries: list[str]) -> str:
    medals_data = get_medals_data(inputFile, countries)

    if not medals_data:
        return ""

    result = ""

    for ind, country in enumerate(medals_data.keys()):
        years = medals_data[country]
        max_year = max(years, key=years.get)
        result += f"{ind + 1}. {country}'s most medals year was: {max_year}, {years[max_year]} medals\n"

    return result

if __name__ == '__main__':
    print(process_overall("data/athlete_events.csv", ["United States", "Ukraine", "Georgia"]))
