import torch.nn.functional as F


def pseudo_label_loss(pred, pseudo):

    return F.mse_loss(pred, pseudo)


def consistency_loss(y1, y2):

    return F.mse_loss(y1, y2)


def entropy_loss(p):

    return -(p * p.log()).mean()