from typing import TypedDict

class InspectionState(TypedDict):
    image_path: str
    thermal_path: str

    latitude: float
    longitude: float

    anomaly: str
    severity: str

    thermal_status: str

    risk_score: int

    report: str