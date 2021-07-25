import unittest
import main

class TestIsPyP(unittest.TestCase):
    def test_wrong_date(self):
        module_response = main.main(['AAC-0122','03/02/2014','18:00:30'])
        sol = 'There is an error on date format'
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_wrong_time(self):
        module_response = main.main(['AAC-0122','03/02/14','18:00:30:25'])
        sol = 'There is an error on time format'
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_r1_cant(self):
        #monday
        module_response = main.main(['AAC-0122','03/02/14','18:00:30'])
        sol = 'Car can not be on the road'
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_r2_cant(self):
        #tuesday
        module_response = main.main(['AAC-0124','07/01/20','11:00:30'])
        sol = 'Car can not be on the road'
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')
    def test_r2_can(self):
        module_response = main.main(['AAC-0122','03/01/20','18:00:30'])
        sol = 'Car can be on the road'
        self.assertEqual(module_response, sol, 
            f'Your solution is {module_response} rather than {sol}')



if __name__ == '__main__':
    unittest.main()