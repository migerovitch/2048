import torch
import numpy as np
from model import *

def train():
    grid = [[0, 0, 0, 0], [4, 2, 0, 0], [8, 2, 2, 0], [32, 16, 8, 4]]

    my_model = MyModel()

    torch.save(my_model.state_dict(), "models/test_model.pt")

    print(my_model(grid))


