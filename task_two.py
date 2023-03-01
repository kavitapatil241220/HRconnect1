"""
Write a program to get "HIRE DATE" of employee who's department id within range 30
to 110 AND who's salary is > 4200.
"""
import csv
import datetime

from typing import Dict
from pprint import pprint


def getdetails(filename:str,value:int)->Dict:
    with open(filename, 'r') as file_obj:
        data = csv.DictReader(file_obj)
        for lines in data:
            if int(lines["SALARY"]) > value and 30 < int(lines["DEPARTMENT_ID"]) < 110:
                hire_date = datetime.datetime.strptime(lines['HIRE_DATE'],"%d-%b-%y")

                #print(hire_date)
                date1 = hire_date.strftime("%Y-%m-%d")
                #print(date1)
                EmployeeData.append({f"Hire date: {date1}, Name: {lines['FIRST_NAME']} {lines['LAST_NAME']} "})
               # EmployeeData.append({"Hire date:", date1, "Name:", lines['FIRST_NAME'] + " " + lines['LAST_NAME'], "emails:" })
    return EmployeeData

if __name__ == "__main__":
    EmployeeData = []
    pprint(getdetails("employees.csv",4200))