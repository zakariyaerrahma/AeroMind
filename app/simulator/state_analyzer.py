from .aircraft import AircraftState


def analyze_state(state: AircraftState) -> list[str]:

    alerts = []

    if state.weather == "Severe":
        alerts.append("Severe weather detected")

    if state.communication == "Degraded":
        alerts.append("Communication system degraded")

    if state.communication == "Lost":
        alerts.append("Communication system lost")

    if state.navigation == "Degraded":
        alerts.append("Navigation system degraded")

    if state.navigation == "Lost":
        alerts.append("Navigation system lost")

    if state.fuel < 25:
        alerts.append("Low fuel level")

    return alerts


def build_rag_query(state: AircraftState) -> str:

    alerts = analyze_state(state)

    if not alerts:
        return "Normal flight operation procedures"

    return " ".join(alerts)