"""
Programmer: Zachary Champion
Project:    jarvis
Project Description:
    Neural net implementation that uses grandmother neurodes, instar learning, forgetting, Hebbian learning, etc.
    It takes in training data to form the weights and then saves that, possibly to a file.
    With that pattern, it will recognize future patterns that are given to it with a probability it outputs that the
    pattern is this classification or that classification.e:
File Description:
    
"""
from random import random


class Neurode:
    def __init__(self, pattern=None):
        self.active = False     # if the neuron is in an active state
        self.act_lvl = 0        # technical activity level
        self.threshold = 0.2    # mysterious threshold???
        # Grandmother" pattern that the neurode will recognize if it ever sees.
        self.grandmother = pattern

    def activate(self, activations, pattern):
        """
        Adjusts activation level and active status.
        Does not return anything, operates completely in-neuron.
        :param activations: list of boolean values corresponding to the activation status of all other main neurons.
        :param pattern: pattern that the neuron receives
        :return:
        """
        # Should check to see if the stimulus is there to see if the activation level should be increased.
        # If not, should decay the activation level according to the last time the stimulus was there.
        # Test to see if the neuron recognizes its own grandmother. Should be the last thing to be checked so that it
        # overrides the rest of everything.
        if pattern == self.grandmother:
            self.act_lvl = 1

        return self.act_lvl >= self.threshold


class NeuralNet:
    def __init__(self, size, training_data):
        """
        :param size: Number of neurodes in the main "net".
        :param training_data: List of data points in whatever form they may take
        """
        self.size = size
        self.grandsons = []
        self.hidden_net = [Neurode for _ in range(size)]
        self.weights = [[random() for _ in self.size] for _ in self.size]
        self.classes = []

        self.train(training_data)

    def train(self, pattern):
        # First, creates "grandmother neurodes" for each training pattern so that it will automatically recognize that
        # specific pattern in the future.
        self.grandsons.append(Neurode(pattern))

    def output(self):
        pass


def build_neural_net():
    print("bullshit")


if __name__ == "__main__":
    build_neural_net()
