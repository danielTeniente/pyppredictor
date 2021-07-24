#should verify that the hour is correct
# the hour should be expressed in 24 h
# format: hh:mm:ss

import re
import datetime

# know if the current plate is in pico y placa


def verify_hour(hour):
    
    # should respect the format
    hour_ex = re.compile(r'\d{2}:\d{2}:\d{2}')
    match_hour = hour_ex.search(hour)
    if(not match_hour or len(hour)!=8):
        return False
    h,m,s = map(int,hour.split(':'))
    is_real_h = h>=0 and h<24
    is_real_m = m>=0 and m<60
    is_real_s = s>=0 and s<60

    return is_real_h and is_real_m and is_real_s


#should verify that the date is correct
# pico y placa doesn't exist before 2010 in Quito
# also, I assume that the current rule will be applied for the next years
# until 2099
# format: dd/mm/yy
def verify_date(date):

    try:
        #if can't pack the values, the format is incorrect
        d,m,y = map(int,date.split('/'))
        #if can't convert the values to a date, the values are incorrect
        datetime.datetime(y, m, d)
    except ValueError:
        return False
    
    is_there_a_rule = y>=10 and y<100

    return is_there_a_rule

# get day of the week inserting the date
def get_day_of_week(date):
    d,m,y = map(int,date.split('/'))
    day = datetime.datetime(y, m, d)
    return day.weekday()+1

# get pico y placa rule inserting the year
# pico y placa rules:
# 1  since 2010 to september 2019: 7:00-9:30, 16:00-19:30 Pico y placa
# 2  since september 2019 to June 2020: 5:00-20:00 Hoy no circula
# 3  since June 2020 to July 2021: 4:00-23:00 Pandemic situation
# 4  July 2021: 7:00-19:00 Hoy no circula
def get_pico_placa_rule(y,m):
    rule = {'id' : 0,
        #(start, ending), (start, ending)...
        'Hours':[(datetime.time(0, 0, 0),datetime.time(0, 0, 0))],
        #key: plates final number
        #value: days of the week
        'Plates':{'':[]}}
    return rule
