import matplotlib.pyplot as plt


def plot_loss(losses):
    """
    Plot the training loss
    :param losses:
    :return:
    """
    plt.plot(losses)
    plt.ylim(0, losses[-1] * 2)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss')
    plt.show()