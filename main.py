import functions

def main(args):
    """
    Use:
    python main.py car_plate date time
    Parameters:
    car_plate: digits of the car's plate
    date: in format dd/mm/yy
    time: in format hh:mm:ss 

    example:
    python main.py AAC-0123 24/07/21 18:52:30
    """
    if len(args) == 3:
        plate = str(args[0])
        date = str(args[1])
        time = str(args[2])
        if(not functions.verify_date(date)):
            return 'There is an error on date format'
        
        if(not functions.verify_hour(time)):
            return 'There is an error on time format'

        #date and time should be correct to this point
        (d,m,y) = functions.get_date_values(date)
        #get the rule 
        rule = functions.get_pico_placa_rule(y,m)
        #get the day of the week
        week_d = functions.get_day_of_week(d,m,y)
        #know the restricte plates for that day
        restriced_plates =  rule['Days'][week_d]
        #get the last number of the plate
        last_n = plate[-1]
        #know if the last number is in pyp
        if(last_n in restriced_plates and 
            functions.time_is_in_pyp(time,rule['Hours'])):
            return 'Car can not be on the road'
        else:
            return 'Car can be on the road'
            


    else:
        print(main.__doc__)        


if __name__ == "__main__":
    import sys
    program_response = main(sys.argv[1:])
    if(program_response):
        print(program_response)