'''
Created on 3 de mai de 2019

@author: zeller
'''
from Neuron.Neuron_Validator.Validator import Validator
from abc import ABC

class Neuron(ABC):
    '''
    Representation of a single Neuron
    '''

    def __init__(self, dendrite_weights, theta, Validator):
        self.dendrite_weights = dendrite_weights
        self.theta = theta
        self.validator = Validator
        self.axions = 0
        self.inputSynapse = 0.0
        self.outputSynapse = 0.0
        
        