import matplotlib.pyplot as plt
import numpy as np

from mapCodeToActivity import mapCodeToActivity
from mapDataToSensor import mapDataToSensor


def plotActivityBySensor(dataFile, activityIndex):
    """
    Plots the activity data for a specific activity index.
    :param dataFile:
    :param activityIndex:
    :return:
    """
    labels = np.load('./data/training/trainLabels.npy')
    data = np.load(f'./data/training/{dataFile}')

    activityLabel = mapCodeToActivity(labels[activityIndex])
    sensor = mapDataToSensor(dataFile)

    plt.plot(data[activityIndex, :])
    plt.title(f"Activity \"{activityLabel}\" - \"{sensor}\"")

    del data
