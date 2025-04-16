import matplotlib.pyplot as plt
from plotActivityBySensor import plotActivityBySensor


def plotActivity(activityIndex):
    """
    Plots the activity data for a specific activity index across all sensors.
    :param activityIndex:
    :return:
    """
    dataFiles = [
        'trainAccelerometer.npy',
        'trainGravity.npy',
        'trainGyroscope.npy',
        'trainJinsAccelerometer.npy',
        'trainJinsGyroscope.npy',
        'trainLinearAcceleration.npy',
        'trainMagnetometer.npy',
        'trainMSAccelerometer.npy',
        'trainMSGyroscope.npy'
    ]

    plt.figure(figsize=(100, 200))
    for index, dataFile in enumerate(dataFiles):
        plt.subplot(9, 1, index + 1)
        plotActivityBySensor(dataFile, activityIndex)

    plt.show()