from datetime import date


def faculty_age():
    today = date.today()
    date_created = date(1969, 5, 5)
    years = today.year - date_created.year
    if today.month < date_created.month or (today.month == date_created.month and today.day < date_created.day):
        years -= 1
    return years
if __name__ == '__main__':
    print(faculty_age())