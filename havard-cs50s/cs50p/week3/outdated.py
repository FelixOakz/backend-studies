"""
1 - prompt for a date in month-dar-year order formatted as 9/8/1636 or september 8, 1636 where month can be any
value in the MONTHS variable
2 - output same date in YYYY-MM-DD format. if user do not input in either format, prompt again.
3 - no month das more than 31d

"""


MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    m, d, y = user_input()
    print(f'{int(y):04}-{int(m):02}-{int(d):02d}')


def user_input():
    while True:
        try:
            date = input('Date: ')
            if '/' in date:
                m, d, y = date.split('/')
            elif ', ' in date:
                m, d, y = date.split(' ')
                m = m.title()
                m = MONTHS.index(m) + 1
                d = d.split(',')[0]
            if int(d) <= 31 and int(m) <= 12:
                return m, d, y
        except (ValueError, IndexError, UnboundLocalError):
            pass


main()
