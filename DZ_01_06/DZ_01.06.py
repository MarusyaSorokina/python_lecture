import json
from random import choice


def gen_person():
    numb = ''
    name = ''
    tel = ''

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    letters = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'k', 'l', 'm', 'n']

    while len(numb) != 10:
        numb += choice(numbers)

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(numbers)

    person = {
        numb: {
            'name': name,
            'tel': tel
        }

    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))

    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
