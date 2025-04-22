import torch

from utils.batch import batch


def predict(model, data, labels, batch_size):
    number_of_batches = data.shape[0] // batch_size
    predictions = None

    with torch.no_grad():
        for i in range(number_of_batches):
            # Get current batch of data
            batch_data, batch_labels = batch(data, labels, batch_size, i)

            # Forward pass
            prediction = model(batch_data)

            if predictions is None:
                predictions = prediction
                continue

            predictions = torch.cat((predictions, prediction), dim=0)

            if i % 12 == 0:
                print(f'Batch {i + 1}/{number_of_batches} processed.')

    return predictions