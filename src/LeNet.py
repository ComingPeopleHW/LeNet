import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.convLayer1 = nn.Sequential(
            nn.Conv2d(1, 6, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2))
        self.convLayer2 = nn.Sequential(
            nn.Conv2d(6, 16, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2))
        self.fcLayer3 = nn.Sequential(
            nn.Linear(16 * 5 * 5, 120),
            nn.ReLU())
        self.fcLayer4 = nn.Sequential(
            nn.Linear(120, 84),
            nn.ReLU())
        self.fcLayer5 = nn.Sequential(
            nn.Linear(84, 10))

    def forward(self, x):
        x = self.convLayer1(x)
        x = self.convLayer2(x)
        x = x.reshape(x.size(0), -1)
        x = self.fcLayer3(x)
        x = self.fcLayer4(x)
        x = self.fcLayer5(x)
        return x


lr = 0.01
net = ConvNet()
input = torch.randn(1, 1, 32, 32)
out = net(input)
y = torch.randn(10).view(1, -1)
criterion = nn.MSELoss()
loss = criterion(out, y)
net.zero_grad()
optimizer = optim.Adam(net.parameters(), lr)
loss.backward()
optimizer.step()
