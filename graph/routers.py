def risk_router(state):

    if state["risk_score"] >= 80:
        return "critical"

    return "normal"