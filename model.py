import torch.nn as nn
import torch
import numpy as np


class MyModel(nn.Module):
    def __init__(self):

        super(MyModel, self).__init__()
        self.lin1 = nn.Linear(16, 16)
        self.lin2 = nn.Linear(16, 16)
        self.lin3 = nn.Linear(16, 4)

    def forward(self, game):
        x = torch.from_numpy(np.array(game).reshape(16))
        x = self.lin1(x.float())
        x = self.lin2(x)
        x = self.lin3(x)
        return self.output(x)

    def output(self, x):
        x = x.tolist()
        return x.index(max(x))
