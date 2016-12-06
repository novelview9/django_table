from django.shortcuts import render

from .custom_day import custom_day
from .load_query import load_query
from .row_by_hour import row_by_hour
from .week_date import week_date


def index(request):

    # today using instead of datetime.datetime.now(pytz.UTC)
    today = custom_day(2016, 11, 17, 8, 11, 39)

    week = week_date(today)

    contents = load_query(week)

    row = row_by_hour(contents)

    return render(
            request,
            'home/index.html',
            context={
                "week": week,
                "row": row,
            })
