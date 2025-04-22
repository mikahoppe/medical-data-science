def accuracy(predicted, labels):
    correct_predictions = (predicted == labels).sum().item()
    accuracy = correct_predictions / labels.size(0) * 100
    return accuracy