"""
Programmer: Zachary Champion
Project:    jarvis
Project Description:
    Neural net implementation that uses grandmother neurodes, instar learning, forgetting, Hebbian learning, etc.
    It takes in training data to form the weights and then saves that, possibly to a file.
    With that pattern, it will recognize future patterns that are given to it with a probability it outputs that the
    pattern is this classification or that classification.
File: NeuralNet.py
File Description:
    Main file with the class definitions for Neurodes, the Neural Net, and a demonstration if the file is called
    directly.
Note - "neurode" is actually a word despite appearances that it is made up.
"""
from scipy.special import expit
from random import random


class Neurode:
    def __init__(self, id, pattern=None):
        self.id = id
        self.active = False  # if the neuron is in an active state
        self.act_lvl = 0  # technical activity level
        self.threshold = 0.2  # mysterious threshold???
        # Grandmother" pattern that the neurode will recognize if it ever sees.
        self.grandmother = pattern

    def introduce_grandmother(self, pattern):
        self.grandmother = pattern

    def activate(self, id, activations, weights, pattern):
        """
        Adjusts activation level and active status.
        Does not return anything, operates completely in-neuron.
        :param activations: list of boolean values corresponding to the activation status of all other main neurons.
        :param pattern: pattern that the neuron receives
        :return:
        """
        # Should check to see if the stimulus is there to see if the activation level should be increased.
        # Test to see if the neuron recognizes its own grandmother.
        if pattern == self.grandmother:
            self.act_lvl = 1
        # If not, should decay the activation level according to the last time the stimulus was there.
        else:
            # Now, the neurode should increase its activation level according to interneurode inputs.
            # Sum up the activations, but only if they are marked as "active" in the list of activations.
            w_sum = sum([weights[id][i] if activations[i] else 0 for i in range(len(activations))]) + self.act_lvl

            # Regularize the activation level with the sigmoid function and set the neurode to that activation level.
            self.act_lvl = expit(w_sum)

        return self.act_lvl >= self.threshold


class NeuralNet:
    def __init__(self, size, training_data):
        """
        :param size: Number of neurodes in the main "net".
        :param training_data: List of data points in whatever form they may take
        """
        self.size = size
        self.hidden_net = [Neurode(i) for i in range(size)]

        # Weights are a 2-dimensional matrix wherein the weight for a particular synapse follows the pattern:
        # weight[to this neurode][from this neurode] where "this neurode" is assumed to be an integer which corresponds
        # to a neurode's ID number. Weights are initialized randomly.
        self.weights = [[random() for _ in self.size] for _ in self.size]

        # Classes is the list of classifications that the neural net is trying to decide between. This could be a string
        # is "offensive" or "not offensive" or something like an image is "red", "green", "blue", etc.
        self.classes = []

        self.train(training_data)

    def train(self, pattern):
        # First, assign a grandson to the pattern - the first neurode found that does not have a grandmother.
        for neurode in self.hidden_net:
            if neurode.grandmother is None:
                neurode.introduce_grandmother(pattern)
                break

        # Then, run the pattern through and adjust the weights according to the error.

    def output(self):
        pass


def build_neural_net():
    print("bullshit")


if __name__ == "__main__":
    build_neural_net()
