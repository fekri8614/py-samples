colors = {
    "lightsalmon": {"R": 255, "G": 160, "B": 122},
    "salmon": {"R": 250, "G": 128, "B": 114},
    "darksalmon": {"R": 233, "G": 150, "B": 122},
    "lightcoral": {"R": 240, "G": 128, "B": 128},
    "indianred": {"R": 205, "G": 92, "B": 92},
    "red": {"R": 255, "G": 0, "B": 0},
}


def closest_color(color: dict):
    main_dict = {'R': 255, 'G': 255, 'B': 255}
    r_value = (color['R'] - main_dict['R']) ** 2
    g_value = (color['G'] - main_dict['G']) ** 2
    b_value = (color['B'] - main_dict['B']) ** 2

    calculated_color = (r_value + g_value + b_value) ** 0.5
    if 0 < calculated_color <= 255:
        return calculated_color
    else:
        return None


print(closest_color(colors['lightsalmon']))
