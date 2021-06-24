from typing import *

import numpy as np
import scipy.special


# dataset: https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png





class NeuronalNet:
    # init the network - default
    def __init__(self, input_nodes :int, hidden_nodes :int, output_nodes :int):
        self.i_nodes = input_nodes
        self.h_nodes = hidden_nodes
        self.o_nodes = output_nodes

        self.w_input_hidden = np.random.rand(self.h_nodes, self.i_nodes) - 0.5
        self.w_hidden_output = np.random.rand(self.o_nodes, self.h_nodes) - 0.5

        self.activiation_function = lambda x : scipy.special.expit(x) # sigmoid


        pass

    def train(self):
        pass

    # input -> ann -> output
    def query(self):
        pass

    def debug_net(self):
        print('w_input_hidden')
        print(self.w_input_hidden)
        print('w_hidden_output')
        print(self.w_hidden_output)

        pass


if __name__ == '__main__':
    nn = NeuronalNet(784, 1000, 10)
    nn.debug_net()



