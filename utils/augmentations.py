import torch


def jitter(x, sigma=0.02):
    noise = torch.randn_like(x) * sigma
    return x + noise


def scaling(x, sigma=0.1):
    factor = torch.randn(x.size(0), 1, 1, 1) * sigma + 1
    return x * factor


def time_mask(x, mask_ratio=0.1):
    T = x.size(2)
    mask_len = int(T * mask_ratio)

    start = torch.randint(0, T - mask_len, (1,))
    x[:, :, start:start + mask_len, :] = 0

    return x