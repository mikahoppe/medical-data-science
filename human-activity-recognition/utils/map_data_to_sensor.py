from .sensors import sensors


def map_data_to_sensor(file_name):
    """
    Maps data file to their corresponding sensor names.
    """
    sensor = [sensor for sensor in sensors if sensor.file_name == file_name]
    return sensor[0] if sensor[0] else "Unknown Sensor"
