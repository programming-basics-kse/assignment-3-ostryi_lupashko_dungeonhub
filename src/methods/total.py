def get_country(my_country: str, info: dict) -> str:
    for key, value in info.items():
        if key in my_country:
            return key

        if my_country in key:
            info[my_country] = value
            del info[key]

        return my_country

def process_total(year):
    with open('../../data/Olympics.tsv', 'r') as file:
        rows = []
        info = {}
        for line in file:
            row = line.strip().split('\t')
            country = get_country(row[6], info)

            if row[9] == year and row[14] != 'NA':
                if country not in info:
                    info[country] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                info[country][row[14]] += 1

    if info == {}:
        return ""

    result = ""
    for country in info:
        result += f"{country} - {info[country]['Gold']} - {info[country]['Silver']} - {info[country]['Bronze']}"
        result += "\n\n"

    return result
#
