import csv
import os
import re

FILENAME = "csvDB.csv"
FIELDNAMES = ['username', 'password']

data = [{
    "username": "",
    "password": ""
}]

def main():
    if os.path.isfile(FILENAME):
        pass
    else:
        with open(FILENAME, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            pass

def userLogin(username, password):
    with open(FILENAME, "r", newline="") as file:
        lines = file.readlines()
        lineChecker = 0
        for line in lines:
            if username in line and password in line:
                pass
            else:
                lineChecker += 1
                if lineChecker == len(lines):
                    raise ValueError

def userCreate(username, password):
    # Check if the password matches the requirements requested on CreateAccount page
    match = re.match('(?=.*[A-Z]){1,}.{4,}[\d]{3,}', password)
    if match:
        data[0]["username"], data[0]["password"] = username, password
        with open(FILENAME, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            for row in data:
                writer.writerow(row)
    else:
        raise ValueError
        