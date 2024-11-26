import csv

if __name__ == '__main__':
    from utils import *
else:
    from .utils import *

def process_interactive(inputFile) -> str:
    country = input("Enter country name: ")

    file_path = get_filepath(inputFile)

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        indexes = get_indexes(header)

        data = []

        for row in reader:
            if country in row[indexes["country"]]:
                data.append({
                    "year": row[indexes["year"]],
                    "city": row[indexes["city"]],
                    "medal": row[indexes["medal"]],
                })

    if not data:
        return f"No data for {country} found."

    first_olympiad_row = min(data, key=lambda x: int(x["year"]))

    result = f"First olympiad for {country} was in {first_olympiad_row['year']} year in {first_olympiad_row['city']}.\n"

    years_data = {}

    for row in data:
        if row['year'] not in years_data:
            years_data[row['year']] = {"bronze": 0, "silver": 0, "gold": 0}

        if row['medal'] == "Bronze":
            years_data[row['year']]["bronze"] += 1
        elif row['medal'] == "Silver":
            years_data[row['year']]["silver"] += 1
        elif row['medal'] == "Gold":
            years_data[row['year']]["gold"] += 1

    years_data = sorted(years_data.items(), key=lambda x: x[1]["gold"] + x[1]["silver"] + x[1]["bronze"])
    the_most_successful = years_data[-1]
    the_least_successful = years_data[0]

    result += f"The most successful olympiad was in {the_most_successful[0]} year with {the_most_successful[1]['gold'] + the_most_successful[1]['silver'] + the_most_successful[1]['bronze']} medals.\n"
    result += f"The least successful olympiad was in {the_least_successful[0]} year with {the_least_successful[1]['gold'] + the_least_successful[1]['silver'] + the_least_successful[1]['bronze']} medals.\n"

    bronze_average = sum(value["bronze"] for key, value in years_data) / len(years_data)
    silver_average = sum(value["silver"] for key, value in years_data) / len(years_data)
    gold_average = sum(value["gold"] for key, value in years_data) / len(years_data)

    result += f"Bronze average: {bronze_average:.2f}, Silver average: {silver_average:.2f}, Gold average: {gold_average:.2f}\n"

    return result

if __name__ == '__main__':
    print(process_interactive())
