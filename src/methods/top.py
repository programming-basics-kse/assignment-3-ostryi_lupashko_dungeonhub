import csv
import pprint

if __name__ == '__main__':
    from utils import *
else:
    from .utils import *

def category_to_str(category):
    categories = ["18-25", "25-35", "35-50", "50+"]
    return categories[category - 1]

def age_to_category(age):
    if age < 25:
        return 1
    elif age < 35:
        return 2
    elif age < 50:
        return 3
    else:
        return 4

def get_best_players(inputFile):
    file_path = get_filepath(inputFile)

    players_medals = {}

    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        header = next(reader)
        indexes = get_indexes(header)

        for row in reader:
            if row[indexes["name"]] not in players_medals:
                name = row[indexes["name"]]
                sex = row[indexes["sex"]]

                players_medals[name] = {
                    "sex": sex,
                    "age": None,
                    "age_category": None,
                    "medals": 0
                }

            if row[indexes["name"]] != "NA":
                name = row[indexes["name"]]

                players_medals[name]["medals"] += 1

            if players_medals[name]["age"] is None:
                if row[indexes["age"]] != "NA":
                    players_medals[name]["age"] = int(row[indexes["age"]]) + (2024 - int(row[indexes["year"]]))
                    players_medals[name]["age_category"] = age_to_category(players_medals[name]["age"])

    for key, value in players_medals.copy().items():
        if value["age"] is None:
            del players_medals[key]

    best_players = {
        "M": {1: {}, 2: {}, 3: {}, 4: {}},
        "F": {1: {}, 2: {}, 3: {}, 4: {}}
    }

    for key, value in players_medals.items():
        our_category = best_players[value["sex"]][value["age_category"]]

        player = {
            "name": key,
            "age": value["age"],
            "medals": value["medals"],
        }

        if not our_category or our_category["medals"] < value["medals"]:
            best_players[value["sex"]][value["age_category"]] = player

    return best_players

def process_top(inputFile, who: list[bool], category: list[int]):
    best_players = get_best_players(inputFile)
    result = ""

    genders = []
    age_categories = []

    if who[0]:
        genders.append("M")
    if who[1]:
        genders.append("F")
    if category[0]:
        age_categories.append(category[0])
    if category[1]:
        age_categories.append(category[1])

    for gender in genders:
        for age_category in age_categories:
            result += f"{best_players[gender][age_category]['name']} is the best {gender} player in {category_to_str(age_category)} category with {best_players[gender][age_category]['medals']}\n"

    return result

if __name__ == '__main__':
    print(process_top('data/Olympics.tsv', [True, True], [1, 2]))
