#should verify that the hour is correct
# the hour should be expressed in 24 h
# format: hh:mm:ss

import re

def verify_hour(hour):
    
    # should respect the format
    hour_ex = re.compile(r'\d{2}:\d{2}:\d{2}')
    match_hour = hour_ex.search(hour)
    if(not match_hour):
        return False
    h,m,s = map(int,hour.split(':'))
    is_real_h = h>=0 and h<24
    is_real_m = m>=0 and m<60
    is_real_s = s>=0 and s<60

    return is_real_h and is_real_m and is_real_s