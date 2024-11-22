import os

country_index = 0
year_index = 0
medal_index = 0
name_index = 0
sport_index = 0
place_index = 0

def get_filepath(filePath):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))  # Go up two levels to `project`
    return os.path.join(project_root, filePath)

def set_indexes(header):
    global country_index, year_index, medal_index, name_index, sport_index, place_index

    country_index = header.index("Team")
    year_index = header.index("Year")
    medal_index = header.index("Medal")
    name_index = header.index("Name")
    sport_index = header.index("Sport")
    place_index = header.index("City")

def get_country(my_country: str, info: dict) -> str:
    for key, value in info.items():
        if key in my_country:
            return key

        if my_country in key:
            info[my_country] = value
            del info[key]

        return my_country
