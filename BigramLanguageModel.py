import torch
import torch.nn as nn
from torch.nn import functional

import chatGptCode
torch.manual_seed(1337)


# Simplest possible neural network
class BigramLanguageModel(nn.module):

    # the initialization method of a PyTorch neural network class that creates an embedding layer for tokens in a language model.
    # input sequence is represented as a unique numerical value called an embedding
    # purpose of this embedding is to enable the model to learn patterns and relationships between tokens in the input sequence.
    # the nn.Embedding function is used to create a lookup table that maps each token to its corresponding embedding vector.

    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)


