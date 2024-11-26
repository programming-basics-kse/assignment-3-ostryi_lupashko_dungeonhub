import csv

if __name__ == '__main__':
    from utils import *
else:
    from .utils import *

def process_medals(inputFile, country: str, year: str):
    file_path = get_filepath(inputFile)

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        info = []
        indexes = get_indexes(header)

        k = 0

        for row in reader:
            if country in row[indexes["country"]] and row[indexes["year"]] == year and row[indexes["medal"]] != 'NA':
                sportsman = {'Name': row[indexes['name']], "Sport": row[indexes['sport']], "Medal": row[indexes['medal']]}
                info.append(sportsman)
                k += 1
                if k == 10:
                    break

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        indexes = get_indexes(header)
        medals_info = {'Gold': 0, 'Silver': 0, 'Bronze': 0}

        for row in reader:
            if row[indexes["year"]] == year and row[indexes["medal"]] != 'NA' and row[indexes["country"]] == country:
                medals_info[row[indexes["medal"]]] += 1

    if not info:
        return ""

    result = "\n=======================\n".join(
        f"Name: {info[i]['Name']}\nSport: {info[i]['Sport']}\nMedal: {info[i]['Medal']}"
        for i in range(0, len(info)))

    result += "\n=======================\n"

    result += f"Total medals: {medals_info['Bronze']} - {medals_info['Silver']} - {medals_info['Gold']}"
    return result

if __name__ == '__main__':
    print(process_medals("data/Olympics.tsv", "Ukraine", "2004"))
