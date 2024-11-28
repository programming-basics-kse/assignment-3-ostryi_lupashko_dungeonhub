import csv

if __name__ == '__main__':
    from utils import *
    from row import Row
else:
    from .utils import *
    from .row import Row

def get_olymp_data(inputFile, country):
    data = []

    with open(get_filepath(inputFile), 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        indexes = get_indexes(header)

        for line in reader:
            row = Row(line, indexes)

            if country in row.get_country():
                data.append({
                    "year": row.get_year(),
                    "city": row.get_city(),
                    "medal": row.get_medal(),
                })

    return data

def get_years_data(olymp_data):
    years_data = {}

    for row in olymp_data:
        if row['year'] not in years_data:
            years_data[row['year']] = {"Bronze": 0, "Silver": 0, "Gold": 0}

        if row['medal'] != "NA":
            years_data[row['year']][row['medal']] += 1

    return years_data

def process_interactive(inputFile) -> str:
    country = input("Enter country name: ")

    olymp_data = get_olymp_data(inputFile, country)

    if not olymp_data:
        return f"No data for {country} found."

    first_olympiad_row = min(olymp_data, key=lambda x: int(x["year"]))
    result = f"First olympiad for {country} was in {first_olympiad_row['year']} year in {first_olympiad_row['city']}.\n"

    years_data = get_years_data(olymp_data)

    calc_total_medals = lambda x: years_data[x]["Gold"] + years_data[x]["Silver"] + years_data[x]["Bronze"]

    the_most_successful = max(years_data, key=calc_total_medals)
    the_least_successful = min(years_data, key=calc_total_medals)

    result += f"The most successful olympiad was in {the_most_successful[0]} year with {calc_total_medals(the_most_successful)} medals.\n"
    result += f"The least successful olympiad was in {the_least_successful[0]} year with {calc_total_medals(the_least_successful)} medals.\n"

    calc_average = lambda medal_type: sum(value[medal_type] for key, value in years_data.items()) / len(years_data)

    result += f"Bronze average: {calc_average('Bronze'):.2f}, Silver average: {calc_average('Silver'):.2f}, Gold average: {calc_average('Gold'):.2f}\n"

    return result

if __name__ == '__main__':
    print(process_interactive("data/athlete_events.csv"))
