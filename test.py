# testing file

from datetime import date
import unittest
import functions 

class TestVerifyHour(unittest.TestCase):
    #testing verify hour function
    def test_vh_hour(self):
        module_response = functions.verify_hour(hour='25:30:17')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_vh_minutes(self):
        module_response = functions.verify_hour(hour='03:65:17')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_vh_seconds(self):
        module_response = functions.verify_hour(hour='12:30:70')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
        
    def test_vh_format(self):
        module_response = functions.verify_hour(hour='20:30:20:20:30')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')

    def test_vh_numbers(self):
        module_response = functions.verify_hour(hour='ab:cd:fg')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')

    def test_vh_correct(self):
        module_response = functions.verify_hour(hour='12:30:25')
        #solution
        sol = True
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')


class TestVerifyDate(unittest.TestCase):
    def test_vd_year(self):
        module_response = functions.verify_date(date='15/04/02')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_vd_day(self):
        module_response = functions.verify_date(date='30/02/10')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_vd_month(self):
        module_response = functions.verify_date(date='15/13/15')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_vd_format(self):
        module_response = functions.verify_date(date='15/06/2008')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_vd_content(self):
        module_response = functions.verify_date(date='hg/55/jo')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_vd_correct(self):
        module_response = functions.verify_date(date='10/09/14')
        #solution
        sol = True
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')

# testing if the function get the correct day
class TestGetDay(unittest.TestCase):
    def test_gd_monday(self):
        module_response = functions.get_day_of_week(d=9,m=7,y=12)
        #solution 1 = monday
        sol = 1
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_gd_tuesday(self):
        module_response = functions.get_day_of_week(1,3,22)
        #solution
        sol = 2
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_gd_friday(self):
        module_response = functions.get_day_of_week(23,7,21)
        #solution
        sol = 5
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_gd_sunday(self):
        module_response = functions.get_day_of_week(5,12,21)
        #solution
        sol = 7
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')

# testing if the function get the correct day
class TestGetDateValues(unittest.TestCase):
    def test_gdv1(self):
        module_response = functions.get_date_values(date='10/09/14')
        sol = (10,9,14)
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_gdv2(self):
        module_response = functions.get_date_values(date='12/5/19')
        #solution
        sol = (12,5,19)
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_gd3(self):
        module_response = functions.get_date_values(date='14/2/22')
        #solution
        sol = (14,2,22)
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')

class TestGetRules(unittest.TestCase):
    def test_gr_1(self):
        module_response = functions.get_pico_placa_rule(14,4)
        #first rule
        rule_id = module_response['id']
        sol = 1
        self.assertEqual(rule_id, sol, 
            f'Your solution is {rule_id} rather than {sol}')
    def test_gr_2(self):
        module_response = functions.get_pico_placa_rule(19,9)
        rule_id = module_response['id']
        sol = 2
        self.assertEqual(rule_id, sol, 
            f'Your solution is {rule_id} rather than {sol}')
    def test_gr_3(self):
        module_response = functions.get_pico_placa_rule(21,1)
        rule_id = module_response['id']
        sol = 3
        self.assertEqual(rule_id, sol, 
            f'Your solution is {rule_id} rather than {sol}')
    def test_gr_4(self):
        module_response = functions.get_pico_placa_rule(22,4)
        rule_id = module_response['id']
        sol = 4
        self.assertEqual(rule_id, sol, 
            f'Your solution is {rule_id} rather than {sol}')
    def test_gr_ranges(self):
        module_response = functions.get_pico_placa_rule(11,4)
        range_number = len(module_response['Hours'])
        sol = 2
        self.assertEqual(range_number, sol, 
            f'Your solution is {range_number} rather than {sol}')
    def test_gr_plates_r4_monday(self):
        module_response = functions.get_pico_placa_rule(22,4)
        #monday
        days_n = module_response['Days'][1]
        sol = ['0','1','2','3']
        self.assertEqual(sorted(days_n), sol, 
            f'Your solution is {days_n} rather than {sol}')
    def test_gr_plates_r4_friday(self):
        module_response = functions.get_pico_placa_rule(22,4)
        #friday
        days_n = module_response['Days'][5]
        sol = ['0','1','8','9']
        self.assertEqual(sorted(days_n), sol, 
            f'Your solution is {days_n} rather than {sol}')

class TestIsPyP(unittest.TestCase):
    def test_earlier(self):
        module_response = functions.time_is_in_pyp(hour='04:59:59',
                            h_ranges=[((5, 0, 0),(20, 0, 0))])
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_in_time(self):
        module_response = functions.time_is_in_pyp(hour='14:30:20',
                            h_ranges=[((7, 0, 0),(19, 0, 0))])
        sol = True
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_in_bet(self):
        module_response = functions.time_is_in_pyp(hour='12:30:30',
                            h_ranges=[((7, 0, 0),(9, 30, 0)),((16,0,0),(19,30,0))])
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')

if __name__ == '__main__':
    unittest.main()
