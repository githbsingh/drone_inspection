import os
import streamlit as st

from graph.workflow import graph

# ----------------------------------
# Setup
# ----------------------------------

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(
    page_title="AegisAI Drone Inspector",
    layout="wide"
)

st.title("🚁 AegisAI - Drone Infrastructure Inspector")

st.markdown(
    """
    Upload:
    - RGB Drone Image
    - Thermal Image
    - GPS Coordinates

    The LangGraph workflow will:
    1. Analyze structural anomalies
    2. Analyze thermal hotspots
    3. Calculate risk
    4. Generate inspection report
    """
)

# ----------------------------------
# Input Section
# ----------------------------------

col1, col2 = st.columns(2)

with col1:
    rgb_file = st.file_uploader(
        "Upload RGB Drone Image",
        type=["jpg", "jpeg", "png"]
    )

with col2:
    thermal_file = st.file_uploader(
        "Upload Thermal Image",
        type=["jpg", "jpeg", "png"]
    )

st.subheader("📍 GPS Information")

latitude = st.number_input(
    "Latitude",
    value=12.9716,
    format="%.6f"
)

longitude = st.number_input(
    "Longitude",
    value=77.5946,
    format="%.6f"
)

# ----------------------------------
# Run Inspection
# ----------------------------------

if st.button("🔍 Run Inspection"):

    if rgb_file is None:
        st.error("Please upload an RGB image.")
        st.stop()

    if thermal_file is None:
        st.error("Please upload a thermal image.")
        st.stop()

    # Save RGB image
    rgb_path = os.path.join(
        UPLOAD_DIR,
        rgb_file.name
    )

    with open(rgb_path, "wb") as f:
        f.write(rgb_file.getbuffer())

    # Save Thermal image
    thermal_path = os.path.join(
        UPLOAD_DIR,
        thermal_file.name
    )

    with open(thermal_path, "wb") as f:
        f.write(thermal_file.getbuffer())

    # Display uploaded images
    st.subheader("Uploaded Images")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            rgb_path,
            caption="RGB Drone Image",
            use_container_width=True
        )

    with col2:
        st.image(
            thermal_path,
            caption="Thermal Image",
            use_container_width=True
        )

    # LangGraph state
    state = {
        "image_path": rgb_path,
        "thermal_path": thermal_path,
        "latitude": latitude,
        "longitude": longitude,
    }

    try:

        with st.spinner("Running LangGraph workflow..."):

            result = graph.invoke(state)

        st.success("Inspection Complete")

        # -----------------------------
        # Results
        # -----------------------------

        st.subheader("Inspection Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Anomaly",
                result.get("anomaly", "N/A")
            )

        with col2:
            st.metric(
                "Severity",
                result.get("severity", "N/A")
            )

        with col3:
            st.metric(
                "Risk Score",
                result.get("risk_score", 0)
            )

        st.subheader("Thermal Analysis")

        st.info(
            result.get(
                "thermal_status",
                "No thermal analysis available"
            )
        )

        st.subheader("Generated Report")

        st.text_area(
            "Inspection Report",
            value=result.get("report", ""),
            height=300
        )

        with st.expander("Full LangGraph State"):
            st.json(result)

    except Exception as e:

        st.error(
            f"Workflow execution failed: {str(e)}"
        )