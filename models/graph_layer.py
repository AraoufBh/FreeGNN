import torch
import torch.nn as nn


class GraphLayer(nn.Module):
   
    def __init__(self, in_dim, out_dim):
        super().__init__()

        self.linear = nn.Linear(in_dim, out_dim)

    def forward(self, h, A):
      
        Ah = torch.matmul(A, h)
        out = self.linear(Ah)

        return out