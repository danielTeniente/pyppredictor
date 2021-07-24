# testing file

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
        module_response = functions.get_day_of_week(date='09/07/12')
        #solution 1 = monday
        sol = 1
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_gd_tuesday(self):
        module_response = functions.get_day_of_week(date='01/03/22')
        #solution
        sol = 2
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_gd_friday(self):
        module_response = functions.get_day_of_week(date='23/07/21')
        #solution
        sol = 5
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_gd_sunday(self):
        module_response = functions.get_day_of_week(date='05/12/21')
        #solution
        sol = 7
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')

# testing if the function get the correct day
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

if __name__ == '__main__':
    unittest.main()
