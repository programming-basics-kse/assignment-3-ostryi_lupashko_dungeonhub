year = '1936'

with open('../../data/Olympics.tsv', 'r') as file:
    rows = []
    info = {}
    for line in file:
        row = line.strip().split('\t')
        if row[9] == year and row[14] != 'NA':
            if row[6] not in info:
                info[row[6]] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
            info[row[6]][row[14]] += 1

for country in info:
    print(f"{country} - {info[country]['Gold']} - {info[country]['Silver']} - {info[country]['Bronze']}", end="\n\n")
#
