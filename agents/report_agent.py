def create_report(state):

    return f"""
Inspection Report

Location:
{state['latitude']},
{state['longitude']}

Anomaly:
{state['anomaly']}

Severity:
{state['severity']}

Thermal:
{state['thermal_status']}

Risk:
{state['risk_score']}
"""