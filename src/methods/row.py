class Row:
    def __init__(self, line, indexes):
        self.line = line
        self.indexes = indexes

    def get_country(self):
        return self.line[self.indexes["country"]]

    def get_year(self):
        return self.line[self.indexes["year"]]

    def get_medal(self):
        return self.line[self.indexes["medal"]]

    def get_name(self):
        return self.line[self.indexes["name"]]

    def get_sport(self):
        return self.line[self.indexes["sport"]]

    def get_city(self):
        return self.line[self.indexes["city"]]

    def get_sex(self):
        return self.line[self.indexes["sex"]]

    def get_age(self):
        return self.line[self.indexes["age"]]

    def has_medal(self):
        return self.get_medal() != "NA"

    def has_age(self):
        return self.get_age() != "NA"

    def calc_age(self):
        if not self.has_age():
            return None

        return int(self.get_age()) + 2024 - int(self.get_year())

