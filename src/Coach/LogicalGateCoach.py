'''
Created on 3 de mai de 2019

@author: zeller
'''
from random import randint

class LogicalGateCoach(object):
    
    LEARNING_RATE = 0.13
    
    def __init__(self, Perceptron, trainset, output):
        self.perceptron = Perceptron
        self.result = [-1] * self.perceptron.input_range
        self.wX = 0
        self.age = 0
        self.error = [-1] * self.perceptron.input_range
        self.trainset = trainset
        self.output = output

    def online_coach(self):
        
        while self.check_ansewer_values() == False:
            self.next_age()
            for index, trainset in enumerate(self.trainset):
                self.wX = self.calculate_weight_sum(trainset, index)
                perceptron_output = self.perceptron.validator.validate(self.wX, self.perceptron.theta)
                self.calculate_error(index, perceptron_output)
                
                if self.error[index] != 0:
                    self.result[index] = perceptron_output
                    self.calculate_dendrite_weight(index)
                    # theta_value = theta_value - LEARNING_RATE * ( output[index] - answer )
                    self.calculate_theta_value(index)  
                else:
                    self.result[index] = perceptron_output
                    
                        
            print(f'Age: {self.age} | Error: {self.error} | Theta: {round(self.perceptron.theta, 2)} | Weights: {self.perceptron.dendrite_weights }')
            for index, value in enumerate(self.result):
                print(f'Perceptron Result: {self.trainset[0], self.trainset[1]} = {value} | Trainset: {self.trainset[0], self.trainset[1]} = {self.output[index]}')
                    
            
    def next_age(self):
        self.age += 1
    
    def check_ansewer_values(self):
        for index, value in enumerate(self.output):
            if self.result[index] != value: 
                return False
            
        return True
    
    def calculate_error(self, index, perceptron_output):
        self.error[index] = self.output[index] - perceptron_output
    
    def calculate_weight_sum(self, trainset, index):
        new_wX_value = 0
        for trainset_index, trainset_value in enumerate(trainset):
            new_wX_value += trainset_value * self.perceptron.dendrite_weights[index][trainset_index]
        
        return new_wX_value
    
    def calculate_dendrite_weight(self, index):
        for index_list, value in enumerate(self.trainset[index]):
                self.perceptron.dendrite_weights[index][index_list] = round( self.perceptron.dendrite_weights[index][index_list] + (value * self.error[index] * self.LEARNING_RATE), 2) 
        
    def calculate_theta_value(self, index):
        self.perceptron.theta = self.perceptron.theta + ( self.error[index] * self.LEARNING_RATE ) 
    