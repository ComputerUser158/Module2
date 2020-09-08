"""
Author: Rawley Collins
Program: camper_age_input


Program takes value from user as integer for years of age and returns age in integer for age in months.
"""

import constants

def convert_to_months(years):
    months = years * constants.MONTHS
    return months


if __name__ == '__main__':
    age_in_years = input("Enter your child's age: ")
    age_in_months = convert_to_months(int(age_in_years))
    print("{} years is {} months".format(age_in_years, age_in_months))
