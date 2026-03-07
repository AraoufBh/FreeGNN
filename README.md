# FreeGNN: Continual Source-Free Graph Neural Network Adaptation for Renewable Energy Forecasting



# Overview

Accurate forecasting of renewable energy generation is essential for efficient grid management and sustainable power planning. However, most machine learning models require access to labeled data from the target site or historical source datasets.

To address this limitation, we propose FreeGNN, a Continual Source-Free Graph Domain Adaptation framework designed for renewable energy forecasting under realistic deployment constraints.

FreeGNN enables models trained on a source domain to adapt to new unseen sites without requiring access to source data or target labels.

The framework integrates several key components:

- Spatio-temporal Graph Neural Network backbone
- Teacher–Student adaptation strategy
- Memory replay mechanism to mitigate catastrophic forgetting
- Graph-based regularization to preserve spatial correlations
- Drift-aware weighting mechanism for dynamic adaptation

These mechanisms allow the model to continuously adapt to non-stationary environmental conditions while maintaining forecasting stability.

# Key Features

✔ Source-free domain adaptation  
✔ Continual learning for streaming renewable data  
✔ Spatio-temporal graph neural network modeling  
✔ Catastrophic forgetting mitigation via memory replay  
✔ Drift-aware adaptation for non-stationary environments  

# Framework

FreeGNN operates in a **continual adaptation setting** where the model:

1. Receives new data from unseen renewable energy sites
2. Adapts without access to the original source dataset
3. Maintains performance via memory replay and teacher–student regularization

# Pipeline: 

<img width="1024" height="570" alt="1772875039291-d8f3cb76-e85d-4b53-a4a9-cc7b6e0b6850_1" src="https://github.com/user-attachments/assets/991b0b13-9b13-4e39-813e-3524c2ce8c62" />

# Paper

The paper is available on arXiv: https://arxiv.org/abs/2603.01657

# Contact

For questions or research collaborations, please contact: Abderaouf Bahi (a.bahi@univ-eltarf.dz)

