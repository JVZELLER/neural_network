'''
Created on 3 de mai de 2019

@author: zeller
'''

import abc

class Validator(abc.ABC):
    '''
    Neuron validator
    '''
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractclassmethod
    def validate(self, sum_input_values, theta):
        """To implement neuron validators"""
        