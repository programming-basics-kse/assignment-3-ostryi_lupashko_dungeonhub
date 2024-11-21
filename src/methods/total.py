def process_total(year):
    with open('../../data/Olympics.tsv', 'r') as file:
        rows = []
        info = {}
        for line in file:
            row = line.strip().split('\t')
            if row[9] == year and row[14] != 'NA':
                if row[6] not in info:
                    info[row[6]] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                info[row[6]][row[14]] += 1

    if info == {}:
        return ""

    result = ""
    for country in info:
        result += f"{country} - {info[country]['Gold']} - {info[country]['Silver']} - {info[country]['Bronze']}"
        result += "\n\n"

    return result
#
