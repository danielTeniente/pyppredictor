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
        module_response = functions.verify_hour(hour='2:0:0')
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
        module_response = functions.verify_date(date='15/04/00')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_vd_day(self):
        module_response = functions.verify_date(date='79/04/10')
        #solution
        sol = False
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_vd_month(self):
        module_response = functions.verify_date(date='15/13/00')
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
    

        
if __name__ == '__main__':
    unittest.main()
