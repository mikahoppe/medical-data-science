class Sensor:
    """
    Class representing a sensor.
    """

    def __init__(self, device, type, sampling_rate, unit):
        self.device = device
        self.type = type
        self.sampling_rate = sampling_rate
        self.unit = unit

    def __repr__(self):
        return f"{self.device} - {self.type} [{self.unit}] ({self.sampling_rate}Hz)"


def mapDataToSensor(fileName):
    """
    Maps data file to their corresponding sensor names.
    """
    data_to_sensor_map = {
        "trainAccelerometer.npy": Sensor("Phone", "Accelerometer", 200, "m/s²"),
        "trainGravity.npy": Sensor("Phone", "Gravity", 200, "m/s²"),
        "trainGyroscope.npy": Sensor("Phone", "Gyroscope", 200, "rad/s"),
        "trainJinsAccelerometer.npy": Sensor("Glasses", "Accelerometer", 20, "m/s²"),
        "trainJinsGyroscope.npy": Sensor("Glasses", "Gyroscope", 20, "rad/s"),
        "trainLinearAcceleration.npy": Sensor("Phone", "Linear Acceleration", 200, "m/s²"),
        "trainMagnetometer.npy": Sensor("Phone", "Magnetometer", 200, "μT"),
        "trainMSAccelerometer.npy": Sensor("Watch", "Accelerometer", 67, "m/s²"),
        "trainMSGyroscope.npy": Sensor("Watch", "Gyroscope", 67, "rad/s"),
    }

    return data_to_sensor_map.get(fileName, "Unknown Sensor")