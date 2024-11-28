import csv

if __name__ == '__main__':
    from utils import *
    from row import Row
else:
    from .utils import *
    from .row import Row

def get_medals_stats(inputFile, year):
    info = {}

    with open(get_filepath(inputFile), 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        indexes = get_indexes(header)

        for line in reader:
            row = Row(line, indexes)
            country = get_country(row.get_country(), info)

            if row.get_year() == year and row.has_medal():
                if country not in info:
                    info[country] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}

                info[country][row.get_medal()] += 1

    return info

def process_total(inputFile, year):
    info = get_medals_stats(inputFile, year)

    if not info:
        return ""

    result = ""

    max_width = max(len(country) for country in info.keys())

    for country in info:
        result += f"{country:<{max_width}}   {info[country]['Gold']} - {info[country]['Silver']} - {info[country]['Bronze']}\n"

    return result[:-1]

if __name__ == '__main__':
    print(process_total("data/athlete_events.csv", "2012"))

