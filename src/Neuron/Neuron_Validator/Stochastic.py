'''
Created on 3 de mai de 2019

@author: zeller
'''
from Validator.Validator import Validator

class Stochastic(Validator):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        
        '''
   
    def validate(self, sum_input_values, theta):
        return 1 if sum_input_values > theta else 0
        