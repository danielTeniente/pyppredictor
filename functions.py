#should verify that the hour is correct
# the hour should be expressed in 24 h
# format: hh:mm:ss

import re
import datetime

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

#get values from date
def get_date_values(date):
    d,m,y = map(int,date.split('/'))
    return (d,m,y)    

# get day of the week inserting the date
def get_day_of_week(d,m,y):
    day = datetime.datetime(y, m, d)
    return day.weekday()+1

# get pico y placa rule inserting the year
# pico y placa rules:
# 1  since 2010 to september 2019: 7:00-9:30, 16:00-19:30 Pico y placa
# 2  since september 2019 to June 2020: 5:00-20:00 Hoy no circula
# 3  since June 2020 to July 2021: 4:00-23:00 Pandemic situation
# 4  July 2021: 7:00-19:00 Hoy no circula
def get_pico_placa_rule(y,m):
    rule = {}
    # july = 7
    if(y>21 or (y==21 and m>6)):
        rule['id'] = 4
            #(start, ending), (start, ending)...
        rule['Hours'] = [((7, 0, 0),(19, 0, 0))]
            #key: days of the week
            #value: final number of plates
        rule['Days'] = {}
        # 4 numbers are restricted each day of the rule
        num_plate = 0
        for i in range(5):
            rule['Days'][i+1] = []
            while(len(rule['Days'][i+1])!=4):
                rule['Days'][i+1].append(str(num_plate)[-1])
                num_plate+=1
            num_plate-=2
    # june = 6
    elif((y==20 and m>5) or y==21):
        rule['id'] = 3
            #(start, ending), (start, ending)...
        rule['Hours'] = [((4, 0, 0),(23, 0, 0))]
            #key: days of the week
            #value: final number of plates
        rule['Days'] = {}
        # restricted even or odd
        for i in range(1,7,2):
            rule['Days'][i] = []
            for j in range(1,10,2):
                rule['Days'][i].append(str(j))
        for i in range(2,7,2):
            rule['Days'][i] = []
            for j in range(0,10,2):
                rule['Days'][i].append(str(j))
    #september = 9
    elif((y==19 and m>8) or y==20):
        rule['id'] = 2
            #(start, ending), (start, ending)...
        rule['Hours'] = [((5, 0, 0),(20, 0, 0))]
            #key: days of the week
            #value: final number of plates
        rule['Days'] = {}
        num_plate = 0
        for i in range(5):
            rule['Days'][i+1] = []
            for _ in range(2):
                rule['Days'][i+1].append(str(num_plate)[-1])
                num_plate+=1
    else:
        rule['id'] = 1
            #(start, ending), (start, ending)...
        rule['Hours'] = [((7, 0, 0),(9, 30, 0)),
                        ((16,0,0),(19,30,0))]
            #key: days of the week
            #value: final number of plates
        rule['Days'] = {}
        num_plate = 0
        for i in range(5):
            rule['Days'][i+1] = []
            for _ in range(2):
                rule['Days'][i+1].append(str(num_plate)[-1])
                num_plate+=1
            
    return rule

# know if the input time is in pico y placa range
def time_is_in_pyp(hour,h_ranges):
    h,m,s = map(int,hour.split(':'))
    is_in_range = False
    for r in h_ranges:
        start = datetime.time(r[0][0], r[0][1], r[0][2])
        end = datetime.time(r[1][0], r[1][1], r[1][2])
        is_in_range |= datetime.time(h,m,s)>=start and datetime.time(h,m,s)<=end
    return is_in_range
