import csv

if __name__ == '__main__':
    from utils import *
else:
    from .utils import *

def process_medals(country: str, year: str):
    file_path = get_filepath("data/Olympics.tsv")

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
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

    result = ""
    if not info:
        return ""

    k = 1
    for i in range(0, len(info)):
        result += f"{k}. Name: {info[i]['Name']},\n"
        result += f"Sport: {info[i]['Sport']},\n"
        result += f"Medal: {info[i]['Medal']}.\n\n"
        result += '=======================\n\n'
        k += 1

    return result

if __name__ == '__main__':
    print(process_medals("United States", "2020"))