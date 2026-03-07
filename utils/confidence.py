import torch


def compute_confidence(y1, y2, sigma=1.0):
    diff = torch.abs(y1 - y2)
    confidence = torch.exp(-diff / sigma)
    return confidence