#!/usr/bin/env python3

import time
import locale
import requests
import datetime


def polish_date():
    locale.setlocale(locale.LC_TIME, 'pl_PL')

    today = datetime.datetime.now()

    day_of_week_name = today.strftime('%A').capitalize()
    day_of_month = today.strftime('%d')
    month_name = today.strftime('%B').capitalize()
    year = today.strftime('%Y')
    return "{} {} {} {}".format(day_of_week_name, day_of_month, month_name, year)


def get_name_day():
    url = "https://nameday.abalin.net/api/V1/today"
    response = requests.get(url)
    name_days = response.json()
    polish_name_day = name_days['nameday']['pl']
    return polish_name_day


x = time.time()

print(polish_date())
print('Imieniny obchodzą dziś:')
print(get_name_day())

y = time.time()

elapsed_time = y - x
print(f'\nElapsed_time: {round(elapsed_time, 5)}')
