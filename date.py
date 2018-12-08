from datetime import timedelta, datetime
import re
today = datetime.now()
print(today.strftime('%d/%m/%Y'))
delt_d = timedelta(days=1)
delt_m = timedelta(days=31)
#насколько я поняла у timedelta нет аргумента months  
yesterday = today - delt_d
tomorrow = today + delt_d
last_m = today - delt_m
print(yesterday.strftime('%d/%m/%Y'))
print(tomorrow.strftime('%d/%m/%Y'))
print(last_m.strftime('%d/%m/%Y'))
ti = '01/01/17 12:10:03.234567'
s = re.sub('\s+', ',',ti)
s = re.sub(r'[^\w\s]','/',s)
#не поняла как запихнуть замену всех знаков препинания на '/' поэтомe сделала это в две строки
l = datetime.strptime(s, '%d/%m/%y/%H/%M/%S/%f')
