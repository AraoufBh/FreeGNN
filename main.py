import torch

from models.freegnn_backbone import FreeGNN
from utils.graph_builder import build_adjacency_matrix, normalize_adjacency

from training.pretrain import pretrain
from training.online_adaptation import adapt_step

from utils.memory_buffer import MemoryBuffer


def main():

    num_nodes = 10
    input_dim = 8
    hidden_dim = 32
    window = 12

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

  
    coords = torch.rand(num_nodes, 2).numpy()

    A = build_adjacency_matrix(coords)
    A = normalize_adjacency(A)

    A = torch.tensor(A, dtype=torch.float32).to(device)

    model = FreeGNN(input_dim, hidden_dim).to(device)


    dataloader = [
        (
            torch.randn(16, num_nodes, window, input_dim).to(device),
            torch.randn(16, num_nodes, 1).to(device),
        )
        for _ in range(20)
    ]

    
    print("Starting multi-source pretraining...")

    pretrain(model, dataloader)

   
    print("Starting online adaptation...")

    buffer = MemoryBuffer(capacity=500)

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

    for step, (x, _) in enumerate(dataloader):

        loss = adapt_step(model, x)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        buffer.add(x.detach().cpu())

        if step % 5 == 0:
            print(f"Step {step} | Adaptation Loss: {loss.item():.4f}")

    
    print("Evaluation completed.")


if __name__ == "__main__":
    main()