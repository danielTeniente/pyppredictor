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
# format: dd/mm/yy
def verify_date(date):
    try:
        #if can't pack the values, the format is incorrect
        d,m,y = map(int,date.split('/'))
        #if can't convert the values to a date, the values are incorrect
        datetime.datetime(y, m, d)
    except ValueError:
        return False
    
    is_there_a_rule = y>=10 

    return is_there_a_rule
