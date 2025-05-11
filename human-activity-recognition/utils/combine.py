import torch

from .sensors import sensors
from .upsample import upsample


def normalize(data):
    """
    Normalize the data
    """
    data = data - data.mean(dim=2, keepdim=True)
    data = data / data.std(dim=2, keepdim=True)
    return data


def combine(is_test=False):
    """
    Combine sensor data into a tensor
    """
    out = None

    for sensor in sensors:
        data = sensor.get_data_as_tensor(test=is_test)
        data = normalize(data)

        if out is None:
            out = data
            continue

        out = torch.cat(upsample(out, data), dim=1)

    return out