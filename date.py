from datetime import timedelta, datetime
today = datetime.now())
print(today.strftime('%d/%m/%Y'))
delt_d = timedelta(days=1)
delt_m = timedelta(days=31)
yesterday = today - delt_d
tomorrow = today + delt_d
last_m = today - delt_m
print(yesterday.strftime('%d/%m/%Y'))
print(tomorrow.strftime('%d/%m/%Y'))
print(last_m.strftime('%d/%m/%Y'))

