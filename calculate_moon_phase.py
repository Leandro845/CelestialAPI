def get_moon_phase_name(fraction):
    """
    Returns the name of the moon phase based on the illuminated fraction.

    Parameters:
    - fraction (float): Illuminated fraction of the moon (should be between 0 and 1).

    Returns:
    - str: Name of the moon phase corresponding to the fraction.
           Possible values: "New Moon", "Waxing Crescent", "First Quarter",
                            "Waxing Gibbous", "Full Moon", "Waning Gibbous",
                            "Last Quarter", "Waning Crescent", "Invalid fraction"
    """
    if 0 <= fraction < 0.01:
        return "New Moon"
    elif 0.01 <= fraction < 0.25:
        return "Waxing Crescent"
    elif 0.25 <= fraction < 0.50:
        return "First Quarter"
    elif 0.50 <= fraction < 0.75:
        return "Waxing Gibbous"
    elif 0.75 <= fraction <= 1.00:
        return "Full Moon"
    elif 1.00 < fraction < 1.25:
        return "Waning Gibbous"
    elif 1.25 <= fraction < 1.50:
        return "Last Quarter"
    elif 1.50 <= fraction < 1.75:
        return "Waning Crescent"
    else:
        return "Invalid fraction"
