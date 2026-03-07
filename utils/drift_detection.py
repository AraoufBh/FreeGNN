import torch


def compute_drift(y_t, y_prev):
    return torch.mean(torch.abs(y_t - y_prev))


def drift_coefficient(drift, gamma=10, delta=0.1):

    return torch.sigmoid(gamma * (drift - delta))