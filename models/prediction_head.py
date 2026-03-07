import torch.nn as nn


class PredictionHead(nn.Module):

    def __init__(self, hidden_dim, out_dim=1):
        super().__init__()

        self.mlp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, out_dim)
        )

    def forward(self, h):
        return self.mlp(h)