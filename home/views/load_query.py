from home.models import User


def load_query(week_date):

        users = User.objects.in_recent_week()

        # wrong:too many query filter- only working on postgresql
        """
        contents = []

        for selected_date in week_date:

            content = {}

            content["week_date"] = selected_date

            user_by_date = users.filter(created_at__date=selected_date)

            contents.append(user_by_date)
            for hour_num in range(23+1):
                user_by_date_time = user_by_date.filter(created_at__hour=hour_num)
                content["hour"] = hour_num
                content["total"] = len(user_by_date_time.all())
                content["android"] = len(user_by_date_time.filter(device__regex=r'^And'))
                content["ios"] = content["total"] - content["android"]
                contents.append(content.copy())
        """

        contents = {}
        contents_in = {
                "total": 0,
                "android": 0,
                "ios": 0,
                }

        for i in range(23+1):
            for j in range(7):
                contents[(i, j)] = contents_in.copy()

        for user in users:
            contents[(user.created_at.hour, week_date.index(user.created_at.date()))]["total"] += 1
            if user.device[:3] == "And":
                contents[(user.created_at.hour, week_date.index(user.created_at.date()))]["android"] += 1
            else:
                contents[(user.created_at.hour, week_date.index(user.created_at.date()))]["ios"] += 1

        return contents
