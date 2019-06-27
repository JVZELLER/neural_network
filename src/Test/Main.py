'''
Created on 26 de jun de 2019

@author: zeller
'''
#===============================================================================
#                                     Imports
#===============================================================================
from Neuron.Perceptron import Perceptron
from Neuron.Neuron_Validator.Stochastic import Stochastic
from Coach.LogicalGateCoach import LogicalGateCoach

#===============================================================================
#                                     Main
#===============================================================================
def and_gate ():
    validator = Stochastic()
    perceptron = Perceptron(4, validator)
    trainset = [[0,0], [0,1], [1,0], [1,1]]
    output = [0, 0, 0, 1]
    coach = LogicalGateCoach(perceptron, trainset, output)
    coach.online_coach()
    
def or_gate ():
    validator = Stochastic()
    perceptron = Perceptron(4, validator)
    trainset = [[0,1],[0,0], [1,0], [1,1]]
    output = [0, 0, 1, 1]
    coach = LogicalGateCoach(perceptron, trainset, output)
    coach.online_coach()
    
def run_demo ():
    and_gate()
    or_gate()
    
    
if __name__ == '__main__':
    run_demo()