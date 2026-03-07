import torch
from torch.optim import Adam


def pretrain(model, dataloader, epochs=10):

    optimizer = Adam(model.parameters(), lr=1e-3)

    for epoch in range(epochs):

        for x, y in dataloader:

            pred = model(x)

            loss = ((pred - y) ** 2).mean()

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch} | Loss {loss.item():.4f}")