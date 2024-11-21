import csv

def process_interactive() -> str:
    country = input("Enter country name: ")

    with open('../../data/Olympics.tsv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)

        YEAR_INDEX = header.index('Year')
        CITY_INDEX = header.index('City')
        MEDAL_INDEX = header.index('Medal')

        data = []

        for row in reader:
            if country in row[6]:
                data.append({
                    "year": row[YEAR_INDEX],
                    "city": row[CITY_INDEX],
                    "medal": row[MEDAL_INDEX]
                })

    if not data:
        return f"No data for {country} found."

    result = "\n\n"
    result += "================"

    first_olympiad_row = min(data, key=lambda x: int(x["year"]))

    result += f"First olympiad for {country} was in {first_olympiad_row['year']} year in {first_olympiad_row['city']}."

    years_data = {}

    for row in data:
        if row['year'] not in years_data:
            years_data[row['year']] = {"bronze": 0, "silver": 0, "gold": 0}

        if row['Medal'] == "Bronze":
            years_data[row['year']]["bronze"] += 1
        elif row['Medal'] == "Silver":
            years_data[row['year']]["silver"] += 1
        elif row['Medal'] == "Gold":
            years_data[row['year']]["gold"] += 1

    years_data = sorted(years_data.items(), key=lambda x: x[1]["gold"] + x[1]["silver"] + x[1]["bronze"])
    the_most_successful = years_data[-1]
    the_least_successful = years_data[0]

    result += f"The most successful olympiad was in {the_most_successful[0]} year with {the_most_successful[1]['gold'] + the_most_successful[1]['silver'] + the_most_successful[1]['bronze']} medals."
    result += f"The least successful olympiad was in {the_least_successful[0]} year with {the_least_successful[1]['gold'] + the_least_successful[1]['silver'] + the_least_successful[1]['bronze']} medals."

    bronze_average = sum(value["bronze"] for key, value in years_data) / len(years_data)
    silver_average = sum(value["silver"] for key, value in years_data) / len(years_data)
    gold_average = sum(value["gold"] for key, value in years_data) / len(years_data)

    result = f"Bronze average: {bronze_average:.2f}, Silver average: {silver_average:.2f}, Gold average: {gold_average:.2f}"

    result += "\n\n"
    result += "================"

    return result
