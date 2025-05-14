import json


def get_all_lines(filepath: str):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    if not lines:
        return []

    return [line.strip() for line in lines]


def load_from_json(path: str):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def save_to_json(path: str, dict_):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data.append(dict_)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def save_list_to_file(filepath: str, list_: list):
    with open(filepath, mode="w", encoding="utf-8") as file:
        for item in list_:
            file.write(f"{item['session_name']}.session\n")
