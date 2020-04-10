import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):

        super(MyModel, self).__init__()
        self.lin1 = nn.Linear(16, 16)
        self.lin2 = nn.Linear(16, 16)
        self.lin3 = nn.Linear(16, 4)

    def forward(self, game):
        x = game
        x = self.lin1(x.float())
        x = self.lin2(x)
        x = self.lin3(x)
        return x
