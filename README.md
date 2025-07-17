# CCFDM
# Curiosity Contrastive Forward Dynamics Model (CCFDM)

## Author  
**S. M. Syed A. Shaihan**  
ID: 2048059  
Supervisor: Prof. Roberto Capobianco  
Collaborator: Federico Di Valerio  

---

## Project Overview

This project explores **sample-efficient reinforcement learning** using **raw pixel observations**. We implement and evaluate a **Curiosity Contrastive Forward Dynamics Model (CCFDM)** to train RL agents for complex control tasks.

The goal is to improve exploration by using **intrinsic rewards** generated through prediction errors from a learned **Forward Dynamics Model (FDM)**, and enhanced with **contrastive learning** techniques.

---

## Key Concepts

- **Curiosity-Driven Exploration**  
  The agent is rewarded based on how "surprised" it is by the outcome of its actions, i.e., how poorly it can predict the next state.

- **Contrastive Learning**  
  Used to align predicted and actual observation features via query-key mechanisms.

- **Forward Dynamics Model (FDM)**  
  Predicts the next state feature given the current state and action. Prediction error drives intrinsic reward.

---

##  Method Overview

### Mechanism

1. **Data Augmentation**: Query and key observations are generated.
2. **Prediction**: FDM predicts next observation features.
3. **Contrastive Learning**: Ensures query and key features align.
4. **Curiosity Module**: Computes intrinsic reward from FDM error.

---

## Training Logs (Partial)

| Episode | Steps | Reward | Batch Reward | Actor Loss | Critic Loss | CURL Loss |
|--------:|------:|-------:|--------------:|-----------:|------------:|----------:|
| 1       | 1000  | 0.0000 | 0.0000        | 0.0000     | 0.0000      | 0.0000    |
| 2       | 2000  | 2.8455 | 0.0032        | -1.2847    | 0.4793      | 2.9239    |
| 4       | 4000  | 2.4560 | 0.0033        | -4.7277    | 0.0107      | 0.7713    |
| 6       | 6000  | 3.6527 | 0.0032        | -7.7729    | 0.0089      | 0.6056    |
| 8       | 8000  | 4.9510 | 0.0041        | -10.2830   | 0.0122      | 0.5119    |
| 10      | 10000 | 2.5611 | 0.0028        | -12.3149   | 0.0103      | 0.3916    |

---

## 🛠️ Implementation Details

- **Framework**: CCFDM-based architecture
- **Training Duration**: ~9 hours
- **Episodes**: 10
- **Hyperparameters**: Based on the research paper, tuned experimentally

---

## 🧪 Results Summary

- Intrinsic motivation via FDM prediction error helps with exploration
- Contrastive learning improves sample efficiency
- Reward improves over time, validating the model's learning capacity


