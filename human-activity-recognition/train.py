from utils.batch import batch


def train(model, optimizer, criterion, data, labels, batch_size, number_of_epochs):
    """
    Train the model
    """
    number_of_batches = data.shape[0] // batch_size
    losses = []

    for epoch in range(number_of_epochs):
        for i in range(number_of_batches):
            # Get current batch of data
            batch_data, batch_labels = batch(data, labels, batch_size, i)

            # Zero the parameter gradients
            optimizer.zero_grad()

            # Forward pass
            outputs = model(batch_data)

            # Compute the loss
            loss = criterion(outputs, batch_labels)

            # Backward pass and optimization
            loss.backward()
            optimizer.step()

            losses.append(loss.item())
            if i % 12 == 0:
                print(
                    f'Epoch [{epoch + 1}/{number_of_epochs}], Step [{i + 1}/{number_of_batches}], Loss: {loss.item():.4f}')

    print("Training complete.")
    return losses
