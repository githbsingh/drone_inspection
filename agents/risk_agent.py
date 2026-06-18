def calculate_risk(
    severity,
    thermal_status
):

    risk = 0

    if severity == "High":
        risk += 70

    if thermal_status == "Hotspot":
        risk += 30

    return risk