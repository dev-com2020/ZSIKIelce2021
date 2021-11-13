import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        print("Poprawny mail")
    else:
        print("Niepoprawny mail")



