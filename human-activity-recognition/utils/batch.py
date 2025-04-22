def batch(data, labels, batch_size, i):
    """
    Get the current batch of data and labels
    """
    start = i * batch_size
    end = (i + 1) * batch_size

    return data[start:end], labels[start:end]