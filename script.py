# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

import logging 
import unittest
from functools import wraps
import time
from random import randint
from statistics import mean, median

class DoMath:
    
    def __init__():
        pass
    
    def execution_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f'Staringt_ {func.__name__}')
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
 
            logging.info(f'End_{func.__name__}')
            logging.info(f'Execution time: {end_time - start_time}')
            return result
        return wrapper
        
    @execution_time
    def average(my_list):

        if my_list:
            logging.info(f'The average is: {sum(my_list) / len(my_list)}')
            return sum(my_list) / len(my_list) 
        
        
        logging.error('the list is empty, please make sur to have at least one element!')
        return None
         
    
    
    def avg():
        my_list = 
        try:
            return sum(my_list) / len(my_list) 
        except ZeroDivisionError as error:
            logging.error('List empty', error)
    
    
    @execution_time
    def average_generator(my_generator):
        counter = 0
        sum_element = 0
        for element in my_generator:
            sum_element += element
            counter += 1
            
        try:
            logging.info(f'The average is: {sum_element / counter}')
            return sum_element / counter
        
        except ZeroDivisionError as error:
            logging.error('the list is empty, please make sur to have at least one element!', error)
            return None
        
        
    def get_numbers():
        for i in range(1,6):
            yield i
            
    
               


class TestDoMath(unittest.TestCase):
    

    
    def test_average(self):
        data = [randint(1,100) for i in range(10)]
        result = DoMath.average(data)
        
        self.assertEqual(result, mean(data))
        
  
    def test_average_emptyList(self):

        result = DoMath.average([])
        
        self.assertIsNone(result)
        
    
    def test_average_generator(self):
        result = DoMath.average_generator(DoMath.get_numbers())
        self.assertEqual(result, 3)
                          
          
        
        
if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    
    unittest.main()
    
    

if __name__ == "__main__":
    unittest.main()