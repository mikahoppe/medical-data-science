import torch

def average_f1_score(predicted, labels):
    f1_score = torch.zeros(labels.unique().numel())
    for i in range(labels.unique().numel()):
        tp = ((predicted == i) & (labels == i)).sum().item()
        fp = ((predicted == i) & (labels != i)).sum().item()
        fn = ((predicted != i) & (labels == i)).sum().item()

        precision = tp / (tp + fp) if tp + fp > 0 else 0
        recall = tp / (tp + fn) if tp + fn > 0 else 0

        f1_score[i] = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0

    average_f1_score = f1_score.mean().item()
    return average_f1_score