from langgraph.graph import StateGraph
from langgraph.graph import END

from graph.state import InspectionState

from graph.nodes import (
    vision_node,
    thermal_node,
    risk_node,
    report_node
)

from graph.routers import (
    risk_router
)

builder = StateGraph(
    InspectionState
)

builder.add_node(
    "vision",
    vision_node
)

builder.add_node(
    "thermal",
    thermal_node
)

builder.add_node(
    "risk",
    risk_node
)

builder.add_node(
    "report_generator",
    report_node
)

builder.set_entry_point(
    "vision"
)

builder.add_edge(
    "vision",
    "thermal"
)

builder.add_edge(
    "thermal",
    "risk"
)

builder.add_conditional_edges(
    "risk",
    risk_router,
    {
        "critical": "report_generator",
        "normal": "report_generator"
    }
)

builder.add_edge(
    "report_generator",
    END
)

graph = builder.compile()