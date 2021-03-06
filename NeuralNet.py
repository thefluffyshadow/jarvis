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
    def __init__(self, ident, pattern=None):
        self.id_num = ident
        self.active = False  # if the neuron is in an active state
        self.act_lvl = 0  # technical activity level
        self.threshold = 0.2
        # Grandmother" pattern that the neurode will recognize if it ever sees.
        self.grandmother = pattern

    def introduce_grandmother(self, pattern):
        self.grandmother = pattern
        

class NeuralNet:
    def __init__(self, size, data):
        """
        :param size: Number of neurodes in the main "net".
        :param data: List of data points in whatever form they may take
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

        self.train(data)

    def train(self, pattern):
        time_delta = 0
        rhythm = range(10000)
        
        for beat in rhythm:
            # First, assign a grandson to the pattern - the first neurode found that does not have a grandmother.
            for neurode in self.hidden_net:
                if neurode.grandmother is None:
                    neurode.introduce_grandmother(pattern)
                    break

            for neurode in self.hidden_net:
                # Should check to see if the stimulus is there to see if the activation level should be increased.
                # Test to see if the neuron recognizes its own grandmother.
                if pattern == neurode.grandmother:
                    neurode.act_lvl = 1
                    time_delta = beat
                        
                # If not, should decay the activation level according to the last time the stimulus was there.
                else:
                    # Create the list of activations - just a list of boolean values corresponding to the neurodes that
                    # are active in this iteration.
                    activations = [n.active for n in self.hidden_net]

                    # Now, the neurode should increase its activation level according to interneurode inputs.
                    # Sum up the activations, but only if they are marked as "active" in the list of activations.
                    w_sum = sum([self.weights[neurode.id_num][i] if activations[i] else 0
                                 for i in range(len(activations))]) + neurode.act_lvl

                    # Decay the activation level according to the time delta since stimulus last occurred.
                    w_sum -= (0 - time_delta) * w_sum
    
                    # Regularize the activation level with the sigmoid function.
                    neurode.act_lvl = expit(w_sum)

    def classify(self, input):
        """
        Takes in the thing to be classified by the neural net and classifies it according to the weights established
        from training.
        :return:
        """
        pass

    def process(self, input):
        """
        Intermediate function that enables the neural net to distinguish between and therefore accept either a single
        item to classify or a list of items to classify.
        :param input:
        :return:
        """
        if type(input) == type([]):
            return [self.classify(item) for item in input]
        else:
            return self.process(input)


if __name__ == "__main__":
    training_data = []
    some_new_data = []

    Brain = NeuralNet(8, training_data)  # Creates and trains the neural network based on some training data.
    Brain.process(some_new_data)
