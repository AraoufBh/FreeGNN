import torch
import torch.nn as nn

from .temporal_encoder import TemporalEncoder
from .graph_layer import GraphLayer
from .prediction_head import PredictionHead


class FreeGNN(nn.Module):
   
    def __init__(self, input_dim, hidden_dim):
        super().__init__()

        self.temporal = TemporalEncoder(input_dim, hidden_dim)
        self.graph = GraphLayer(hidden_dim, hidden_dim)
        self.head = PredictionHead(hidden_dim)

    def forward(self, x, A):

        h = self.temporal(x)
        h = self.graph(h, A)
        y = self.head(h)

        return y