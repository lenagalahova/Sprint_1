times_str = '1h 45m,360s,25m,30m 120s,2h 60s'

times_str = times_str.replace(',', ' ')
times = times_str.split(' ')
i = 0


for time in times:
    if 'h' in time:
        time = int(time.replace('h', ' '))
        i = time * 60 + i
    elif 's' in time:
        time = int(time.replace('s', ' '))
        if time % 60 == 0:
            i = time//60 + i
    else:
        time = int(time.replace('m', ' '))
        i += time
print(i)
