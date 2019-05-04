'''
Created on 3 de mai de 2019

@author: zeller
'''

class Neuron():
    '''
    Representation of a single Neuron
    '''

    def __init__(self, dendrite_weights, theta, validator, axions):
        self.dendrite_weights = dendrite_weights
        self.theta = theta
        self.validator = validator
        self.axions = axions 
        
        