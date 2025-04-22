import torch

from .sensors import sensors
from .upsample import upsample


def combine(is_test=False):
    """
    Combine sensor data into a tensor
    """
    out = None

    for sensor in sensors:
        data = sensor.get_data_as_tensor(test=is_test)

        if out is None:
            out = data
            continue

        out = torch.cat(upsample(out, data), dim=1)

    return out