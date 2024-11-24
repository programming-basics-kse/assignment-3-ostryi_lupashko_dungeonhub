import os

def get_filepath(filePath):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))  # Go up two levels to project root
    return os.path.join(project_root, filePath)

def get_indexes(header):
    return {
        "country": header.index("Team"),
        "year": header.index("Year"),
        "medal": header.index("Medal"),
        "name": header.index("Name"),
        "sport": header.index("Sport"),
        "city": header.index("City"),
    }

def get_country(my_country: str, info: dict) -> str:
    if not info:
        return my_country

    for key, value in list(info.items()):
        if key in my_country:
            return key

        if my_country in key:
            info[my_country] = value
            del info[key]

            return my_country

    return my_country
