# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

import logging 
import unittest
from functools import wraps
import time

class DoMath:
    
    def __init__():
        pass
    
    
    def execution_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f'{func.__name__} _Execution time: {end_time - start_time}')
            return result
        return wrapper
            
    
    
    @execution_time
    def average(my_list):
        out = None
        if len(my_list) >0:
            out = sum(my_list) / len(my_list) 
        else:
            logging.error('the list is empty, please make sur to have at least one element!')
            
        return out
        
    
    @execution_time
    def average_generator(my_generator):
        counter = 0
        sum_element = 0
        for element in my_generator:
            sum_element += element
            counter += 1
            
        try:
            return sum_element / counter
        
        except ZeroDivisionError as error:
            logging.error('the list is empty, please make sur to have at least one element!', error)
            return None
        
    def get_numbers():
        for i in range(1,6):
            yield i


class TestDoMath(unittest.TestCase):
    def test_average(self):
        data = [1,2,3,4,5]
        result = DoMath.average(data)
        
        self.assertEqual(result, 3)
  
    def test_average_emptyList(self):

        result = DoMath.average([])
        
        self.assertIsNone(result)
    
    def test_average_generator(self):
        result = DoMath.average_generator(DoMath.get_numbers())
        self.assertEqual(result, 3)
                          
          
        
        
if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    logging.info("starting...")
    print("+++++++++++++++++++++++++++")
    #unittest.main()
    print(DoMath.average([1,2,3,4,5]) == 3)
    print(DoMath.average([]) == None)
    print(DoMath.average_generator(DoMath.get_numbers()) == 3)
    print("==========================")
    logging.info('###### End')