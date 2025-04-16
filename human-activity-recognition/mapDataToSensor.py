def mapDataToSensor(fileName):
    """
    Maps data file to their corresponding sensor names.
    """
    data_to_sensor_map = {
        "trainAccelerometer.npy": "Phone - Accelerometer (200Hz)",
        "trainGravity.npy": "Phone - Gravity (200Hz)",
        "trainGyroscope.npy": "Phone - Gyroscope (200Hz)",
        "trainJinsAccelerometer.npy": "Glasses - Accelerometer (20Hz)",
        "trainJinsGyroscope.npy": "Glasses - Gyroscope (20Hz)",
        "trainLinearAcceleration.npy": "Phone - Linear Acceleration (200Hz)",
        "trainMagnetometer.npy": "Phone - Magnetometer (50Hz)",
        "trainMSAccelerometer.npy": "Watch - Accelerometer (67Hz)",
        "trainMSGyroscope.npy": "Watch - Gyroscope (67Hz)",
    }

    return data_to_sensor_map.get(fileName, "Unknown Sensor")