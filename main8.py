from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    #  Реалізуйте тут домашнє завдання

    dict_births = {}
    today = datetime(year=2023, month=12, day=26).date()    # Встановлення статичної дати замість стогоднішньої
    # today = datetime.today().date()                       # Встановлення сьогоднішної дати 

    time_delta = timedelta(days=7)
    date_end = today + time_delta

    for dict_user in users:
        for day_match in range(0, time_delta.days):
            dat_delta = timedelta(days=day_match)
            dat_birth = dict_user['birthday']

            if dict_user['birthday'].year == (dict_user['birthday']-dat_delta).year:    # Перевірка, чи переходить Дельта із року в рік
                dat_birth = datetime(
                    year=today.year, month=dat_birth.month, day=dat_birth.day)
            else:
                dat_birth = datetime(
                    year=today.year+1, month=dat_birth.month, day=dat_birth.day)

            if dat_birth.date() == today + dat_delta:                                   # Перевіряє пранлежність кожного ДН до відповідного
                if (today+dat_delta).strftime('%A') == 'Monday':                        # дня тижня, та формує вихідний список
                    if ('Monday') not in dict_births:
                        dict_births['Monday'] = []
                    dict_births['Monday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Tuesday':
                    if ('Tuesday') not in dict_births:
                        dict_births['Tuesday'] = []
                    dict_births['Tuesday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Wednesday':
                    if ('Wednesday') not in dict_births:
                        dict_births['Wednesday'] = []
                    dict_births['Wednesday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Thursday':
                    if ('Thursday') not in dict_births:
                        dict_births['Thursday'] = []
                    dict_births['Thursday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Friday':
                    if ('Friday') not in dict_births:
                        dict_births['Friday'] = []
                    dict_births['Friday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Saturday':
                    if ('Monday') not in dict_births:
                        dict_births['Monday'] = []
                    dict_births['Monday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Sunday':
                    if ('Monday') not in dict_births:
                        dict_births['Monday'] = []
                    dict_births['Monday'].append(dict_user['name'])
                    break

    return dict_births


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 9, 1).date()},
        ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
