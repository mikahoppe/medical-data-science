import numpy as np
import torch

class Sensor:
    """
    Class representing a sensor.
    """

    def __init__(self, device, type, sampling_rate, unit, fileName):
        self.device = device
        self.type = type
        self.sampling_rate = sampling_rate
        self.unit = unit
        self.fileName = fileName

    def __repr__(self):
        return f"{self.device} - {self.type} [{self.unit}] ({self.sampling_rate}Hz)"

    def get_data_as_tensor(self, test=False):
        return torch.transpose(torch.from_numpy(np.load(f'./data/{"testing" if test else "training"}/{"test" if test else "train"}{self.fileName}.npy')), 1, 2)


sensors = [
    Sensor("Phone", "Accelerometer", 200, "m/s²", "Accelerometer"),
    Sensor("Phone", "Gravity", 200, "m/s²", "Gravity"),
    Sensor("Phone", "Gyroscope", 200, "rad/s", "Gyroscope"),
    Sensor("Glasses", "Accelerometer", 20, "m/s²", "JinsAccelerometer"),
    Sensor("Glasses", "Gyroscope", 20, "rad/s", "JinsGyroscope"),
    Sensor("Phone", "Linear Acceleration", 200, "m/s²", "LinearAcceleration"),
    Sensor("Phone", "Magnetometer", 200, "μT", "Magnetometer"),
    Sensor("Watch", "Accelerometer", 67, "m/s²", "MSAccelerometer"),
    Sensor("Watch", "Gyroscope", 67, "rad/s", "MSGyroscope"),
]