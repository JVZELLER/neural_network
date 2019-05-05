#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Neuron.Neuron import Neuron

## Imports
from random import randint

class Perceptron(Neuron):
    
    def __init__(self, input_range, Validator):
        self.input_range = input_range
        super().__init__([ [randint(0, 10) for i in range(2)] ] * self.input_range, randint(0, 10), Validator)