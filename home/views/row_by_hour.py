def row_by_hour(contents):

    return [[contents[(hour, day)] for day in range(7)] for hour in range(24)]
