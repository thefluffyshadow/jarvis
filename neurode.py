"""
Programmer: Zachary Champion
Project:    jarvis
Project Description:
    Neural network implementation
File:       neuron.py
File Description:
    Description of an individual neuron.
"""


class Neurode:
    def __init__(self, time):
        self.activated = False
        self.a_ = 0
        self.threshold = 0.2
