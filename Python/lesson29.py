import json
from random import choice


def get_person():
    name = ""
    tel = ""

    letters = ["a", "b", "c", "d", "e", "f", "e", "g"]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        "name": name,
        "tel": tel
    }
    return person


def write_json(person_dict, key):
    try:
        data = json.load(open("person.json"))
    except FileNotFoundError:
        data = {}

    data[key] = person_dict
    with open("person.json", "w") as f:
        json.dump(data, f, indent=2)


def random_num():
    key = ""
    while len(key) != 10:
        key += choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    return key


for i in range(5):
    write_json(get_person(), random_num())
