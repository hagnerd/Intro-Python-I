"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the
file) and not prompted input. Also, the brackets around year are to denote that
the argument is optional, as this is a common convention in documentation.

This would mean that from the command line you would call
`python3 14_cal.py 4 2015` to print out a calendar for April in 2015, but if
you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime
import functools


def get_year(date=datetime.now()):
    """
    Gets the year from the date passed in, with a default of the current
    date.
    """
    return date.year


def get_month(date=datetime.now()):
    """
    Gets the month from the date passed in, with a default of the current date.
    """
    return date.month


def get_current_year_and_month():
    """ gets the current date and year if the user doesn't provide any """
    return (get_year(), get_month())


def get_cal_header(year, month):
    """ whatever """
    month_name = calendar.month_name[month]
    week_header = calendar.weekheader(2)
    week_header_len = len(week_header)
    top_header = f"{month_name}, {year}".center(week_header_len, ' ')
    return f"{top_header}\n{week_header}"


def create_month(acc, w):
    next_week = functools.reduce(create_week, w, "")
    next_val = f"{next_week}" if acc == "" else f"{acc}\n{next_week}"
    return next_val

def create_week(acc, date):
    val = str(date.day).rjust(2, '0')
    n_val = f"{val}" if acc == "" else f"{acc} {val}"
    return n_val

def create_cal_days(year, month):
    cal = calendar.Calendar()
    return functools.reduce(create_month, cal.monthdatescalendar(year, month),
                            "")

def create_cal():
    if len(sys.argv) == 1:
        year, month = get_current_year_and_month()
    elif len(sys.argv) == 2:
        _, m = sys.argv
        month = int(m)
        year = get_year()
    elif len(sys.argv) == 3:
        _, m, y = sys.argv
        year = int(y)
        month = int(m)
    else:
        print("""Expected either no argument, for the current month and date, a
single argument for a month in the current year, or two arguments
for the month and year you would like printed out""")
        return
    header = get_cal_header(year, month)
    cal = create_cal_days(year, month)
    print(f"{header}\n{cal}")


create_cal()
