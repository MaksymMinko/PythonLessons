s = int(input('Enter seconds: '))
if s >= 86400:
    days = s // 86400
    hours = (s - days * 86400) // 3600
    minutes = (s - days * 86400 - hours * 3600) // 60
    sec = s - days * 86400 - hours * 3600 - minutes * 60
    print(days, 'd', hours, 'h', minutes, 'm', sec, 'sec')
elif s >= 3600:
    hours = s // 3600
    minutes = (s - hours * 3600) // 60
    sec = s - hours * 3600 - minutes * 60
    print(hours, 'h', minutes, 'm', sec, 'sec')
elif s >= 60:
    minutes = s // 60
    sec = s - minutes * 60
    print(minutes, 'm', sec, 'sec')
elif s > 0:
    print(s, 'sec')
else:
    print('The value is incorrect!')
