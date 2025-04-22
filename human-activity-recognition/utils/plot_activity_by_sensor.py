import matplotlib.pyplot as plt
import numpy as np

from .map_code_to_activity import map_code_to_activity
from .map_data_to_sensor import map_data_to_sensor


def plot_activity_by_sensor(data_file, activity_index):
    """
    Plots the activity data for a specific activity index.
    :param data_file:
    :param activity_index:
    :return:
    """
    labels = np.load('../data/training/trainLabels.npy')
    data = np.load(f'./data/training/{data_file}')

    activity_label = map_code_to_activity(labels[activity_index])
    sensor = map_data_to_sensor(data_file)

    plt.plot(data[activity_index, :])
    plt.title(f"Activity \"{activity_label}\" - \"{sensor}\"")

    del data
