#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Neuron.Neuron import Neuron

## Imports
from random import randint

class Perceptron(Neuron):
    
    def __init__(self, input_range):
        self.theta = randint(0, 10)
        self.input_range = input_range
        self.dendrite_weights = [randint(0, 10)] * input_range 