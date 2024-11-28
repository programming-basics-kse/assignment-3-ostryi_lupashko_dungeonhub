import csv

if __name__ == '__main__':
    from utils import *
    from row import Row
else:
    from .utils import *
    from .row import Row

class Player:
    def __init__(self, row):
        self.sex = row.get_sex()
        self.age_category = None
        self.age = None
        self.set_age(row.calc_age())
        self.medals = 0
        self.name = row.get_name()

    def increase_medals(self):
        self.medals += 1

    def get_age_category(self):
        if self.age < 25:
            return 1
        elif self.age < 35:
            return 2
        elif self.age < 50:
            return 3
        else:
            return 4

    def age_category_to_string(self):
        categories = ["18-25", "25-35", "35-50", "50+"]
        return categories[int(self.age_category) - 1]

    def get_medals(self):
        return self.medals

    def has_age(self):
        return self.age is not None

    def set_age(self, age: int):
        self.age = age

        if self.has_age():
            self.age_category = self.get_age_category()

    def get_sex(self):
        return self.sex

    def get_name(self):
        return self.name

def get_players_stats(inputFile):
    players_medals = {}

    with open(get_filepath(inputFile), 'r') as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)
        indexes = get_indexes(header)

        for line in reader:
            row = Row(line, indexes)

            if row.get_name() not in players_medals:
                player = Player(row)
            else:
                player = players_medals[row.get_name()]

            if row.has_medal():
                player.increase_medals()

            if not player.has_age() and row.has_age():
                player.set_age(row.calc_age())

            players_medals[row.get_name()] = player

    return {key: value for key, value in players_medals.copy().items() if value.has_age()}

def get_best_players(inputFile):
    players_stats = get_players_stats(inputFile)

    best_players = {
        "M": {1: {}, 2: {}, 3: {}, 4: {}},
        "F": {1: {}, 2: {}, 3: {}, 4: {}}
    }

    for key, player in players_stats.items():
        current_best = best_players[player.get_sex()][player.get_age_category()]

        if not current_best or current_best.get_medals() < player.get_medals():
            best_players[player.get_sex()][player.get_age_category()] = player

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
            player = best_players[gender][age_category]
            result += f"{player.get_name()} is the best {gender} player in {player.age_category_to_string()} category with {player.get_medals()}\n"

    return result

if __name__ == '__main__':
    print(process_top('data/athlete_events.csv', [True, True], [2, 3]))
