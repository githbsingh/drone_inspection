from agents.vision_agent import analyze_image
from agents.thermal_agent import analyze_thermal
from agents.risk_agent import calculate_risk
from agents.report_agent import create_report


def vision_node(state):

    result = analyze_image(
        state["image_path"]
    )

    state["anomaly"] = result["anomaly"]
    state["severity"] = result["severity"]

    return state


def thermal_node(state):

    state["thermal_status"] = analyze_thermal(
        state["thermal_path"]
    )

    return state


def risk_node(state):

    state["risk_score"] = calculate_risk(
        state["severity"],
        state["thermal_status"]
    )

    return state


def report_node(state):

    state["report"] = create_report(
        state
    )

    return state