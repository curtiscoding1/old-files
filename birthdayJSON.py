import json

birthdays =  {"curtis": "05/09/1999",
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

with open("info.json", "w") as bdayfile:
    json.dump(birthdays, bdayfile)
with open("info.json", "r") as readbdayfile:
    info = json.load(readbdayfile)

name = input("whos birthday do you want to know?")
print(info[name])