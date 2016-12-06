from datetime import timedelta


def week_date(today):

    return [
            today.date()
            if week_num == 0 else
            (today - timedelta(week_num)).date()
            for week_num in reversed(range(6+1))
    ]
