"""
Write a program to get details of employees who's salary is > 9000. The output should
be in following format
"""
import csv

from typing import Dict
from pprint import pprint

def get_data_info(filename:str, value:int) -> Dict:

    with open(filename, 'r') as file_obj:
        data = csv.DictReader(file_obj)
        for lines in data:
            if int(lines["SALARY"]) > value:
                phonenumber = lines['PHONE_NUMBER'].split('.')
                phonenumber = "".join(phonenumber)
                EmployeeData.append({"Name": lines['FIRST_NAME'] + " " + lines['LAST_NAME'],
                                     "emails": lines['EMAIL'], "phone number": phonenumber})

    return EmployeeData

if __name__ == "__main__":
    EmployeeData = []
    pprint(get_data_info("employees.csv", 9000))
    """
    testing is going on
    """