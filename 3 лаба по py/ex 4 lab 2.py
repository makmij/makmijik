from datetime import datetime, timedelta

while True:
    try:
        birthday = input("Введите дату вашего рождения в формате ГГГГ-ММ-ДД: ")
        birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
        break
    except ValueError:
        print("Некорректный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")
future_date_10000_days = birthday_date + timedelta(days=10000)
future_date_1000000_minutes = birthday_date + timedelta(minutes=1000000)
future_date_1000000000_seconds = birthday_date + timedelta(seconds=1000000000)
print("10 000 дней будет в", future_date_10000_days.strftime("%Y-%m-%d"))
print("1 000 000 минут будет в", future_date_1000000_minutes.strftime("%Y-%m-%d"))
print("1 000 000 000 секунд будет в", future_date_1000000000_seconds.strftime("%Y-%m-%d"))