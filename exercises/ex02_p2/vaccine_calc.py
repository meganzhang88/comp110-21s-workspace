"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730237266"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    date: str = future_date(days)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + date + ".")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Returns the number of days until reaching the target percent vaccinated."""
    target_doses: int = round(population * (target / 100)) * 2
    doses_left: int = target_doses - doses
    days_needed: int = round(doses_left / doses_per_day)
    return days_needed


# TODO 3: Define future_date function
def future_date(days_needed: int) -> str:
    """Returns a string representation of the date that is x number of days from now."""
    completion_date: datetime = datetime.today() + timedelta(days_needed)
    return completion_date.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()
