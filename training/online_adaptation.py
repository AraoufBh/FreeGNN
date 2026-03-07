import torch

from utils.augmentations import jitter, scaling
from utils.confidence import compute_confidence


def adapt_step(model, x):

    x1 = jitter(x)
    x2 = scaling(x)

    y1 = model(x1)
    y2 = model(x2)

    conf = compute_confidence(y1, y2)

    pseudo = (y1 + y2) / 2

    loss = ((y1 - pseudo) ** 2 * conf).mean()

    return loss