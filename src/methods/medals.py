import csv

if __name__ == '__main__':
    from utils import *
    from row import Row
else:
    from .utils import *
    from .row import Row

def get_best_players(inputFile, country, year):
    info = []

    with open(get_filepath(inputFile), 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        indexes = get_indexes(header)

        line = next(reader)

        while line and len(info) != 10:
            row = Row(line, indexes)

            if country in row.get_country() and row.get_year() == year and row.has_medal():
                info.append({
                    'Name': row.get_name(),
                    "Sport": row.get_sport(),
                    "Medal": row.get_medal()
                })

            line = next(reader)

    return info

def get_medals_stats(inputFile, country, year):
    medals_info = {'Gold': 0, 'Silver': 0, 'Bronze': 0}

    with open(get_filepath(inputFile), 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        indexes = get_indexes(header)

        for line in reader:
            row = Row(line, indexes)

            if row.get_year() == year and row.has_medal() and country in row.get_country():
                medals_info[row.get_medal()] += 1

    return medals_info

def process_medals(inputFile, country: str, year: str):
    players_info = get_best_players(inputFile, country, year)
    medals_info = get_medals_stats(inputFile, country, year)

    if not players_info:
        return ""

    result = ""

    for player in players_info:
        result += f"Name: {player['Name']}\nSport: {player['Sport']}\nMedal: {player['Medal']}"
        result += "\n=======================\n"

    result += f"Total medals: {medals_info['Bronze']} - {medals_info['Silver']} - {medals_info['Gold']}"

    return result

if __name__ == '__main__':
    print(process_medals("data/athlete_events.csv", "Ukraine", "2004"))
