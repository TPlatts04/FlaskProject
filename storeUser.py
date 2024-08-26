import re
from app import db, session

def userCreate(usrClass):
    # Check if the password matches the requirements requested on CreateAccount page
    match = re.match('(?=.*[A-Z]){1,}.{4,}[\d]{3,}', usrClass.password)
    if match:
        pass
    else:
        raise ValueError
        