import torch
import torch.nn as nn


class TemporalEncoder(nn.Module):
   
    def __init__(self, input_dim, hidden_dim):
        super().__init__()

        self.gru = nn.GRU(input_dim, hidden_dim, batch_first=True)

    def forward(self, x):
       
        B, N, T, F = x.shape

        x = x.reshape(B * N, T, F)

        out, _ = self.gru(x)

        h = out[:, -1, :]
        h = h.reshape(B, N, -1)

        return h