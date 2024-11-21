country = "Spain"
year = "1937"

def process_medals(country: str, year: str):

    with open('../../data/Olympics.tsv', 'r') as file:
        rows = []
        info = []
        k = 0
        for line in file:
            row = line.strip().split('\t')
            if country in row[6] and row[9] == year and row[14] != 'NA':
                sportsman = [row[1], row[12], row[14]]
                info.append(sportsman)
                k += 1
                if k == 10:
                    break

    result = ""
    if info == []:
        return ""

    k = 1
    for i in range(0, len(info)):
        result += f"{k}. Name: {info[i][0]},"
        result += '\n'
        result += f"Sport: {info[i][1]},"
        result += '\n'
        result += f"Medal: {info[i][2]}."
        result += '\n'
        result += '\n'
        result += '======================='
        result += '\n'
        result += '\n'
        k += 1

    return result


print(process_medals(country, year))
#
