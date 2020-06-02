from datetime import datetime

from django.shortcuts import render
import requests
import csv


# Create your views here.
def index(request):
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    r = requests.get(url)
    # This decode the text in UTF-8 formate
    f = (line.decode('utf-8') for line in r.iter_lines())
    reader = list(csv.reader(f))

    lists = []
    total = 0
    previous = 0

    # This print all the Cases of Corona rest of the world

    for row in reader[1:]:
        temp = {
            'province': row[0],
            'country': row[1],
            'affected_people': row[-1],
            'death': row[2],
        }

        total += int(row[-1])
        previous += int(row[-2])
        lists.append(temp)
        date = datetime.now()

    # Print value for individual country

    for row in reader[1:]:
        if row[1] == 'Bangladesh':
            bangladesh = row[-1]
        if row[1] == 'Italy':
            italy = row[-1]
            Previous_italy = row[-2]

    context = {
        'total': total,
        'previous': previous,
        'corona': lists,
        'date': date,
        'bangladesh': bangladesh,
        'italy': italy,
        'Previous_italy': Previous_italy
    }
    return render(request, 'index.html', context)

