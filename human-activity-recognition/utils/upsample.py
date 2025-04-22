import torch.nn.functional as F


def upsample(x, y):
    frequency_x = x.shape[2]
    frequency_y = y.shape[2]

    frequency_target = max(frequency_x, frequency_y)

    out_x = x
    out_y = y

    # Upsample x if its frequency is less than the target frequency
    if frequency_x < frequency_target:
        out_x = F.interpolate(
            x,
            size=frequency_target,
            mode='linear',
        )

    # Upsample y if its frequency is less than the target frequency
    if frequency_y < frequency_target:
        out_y = F.interpolate(
            y,
            size=frequency_target,
            mode='linear',
        )

    return out_x, out_y