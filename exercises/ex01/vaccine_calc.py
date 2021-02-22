"""A vaccination calculator."""

__author__ = "730237266"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent_vaccinated: int = int(input("Target percent vaccinated: "))

target_doses: int = round(population * (target_percent_vaccinated/100)) * 2
doses_left: int = target_doses - doses_administered
days_needed: int = round(doses_left / doses_per_day)

completion_date: datetime = datetime.today() + timedelta(days_needed)

print("We will reach " + str(target_percent_vaccinated) + "% vaccination in " + str(days_needed) + " days, which falls on " + completion_date.strftime("%B %d, %Y") + ".")