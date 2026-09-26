import streamlit as st
import pandas as pd

from app.simulator.scenarios import normal_scenario
from app.simulator.engine import FlightSimulator

from app.simulator.state_analyzer import (
    analyze_state,
    build_rag_query
)

from app.rag.retriever import DocumentRetriever
from app.llm.client import LLMClient


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AeroMind",
    page_icon="✈️",
    layout="wide"
)


# ==================================================
# TITLE
# ==================================================

st.title("✈️ AeroMind")

st.subheader(
    "LLM-Powered Aviation Simulation & RAG System"
)

st.info(
    "⚠️ AeroMind is a simulated training environment. "
    "It does not use real aircraft data and is not "
    "intended for real-world aviation operations."
)


# ==================================================
# INITIALIZATION
# ==================================================

if "simulator" not in st.session_state:

    aircraft = normal_scenario()

    st.session_state.simulator = FlightSimulator(
        aircraft
    )


# Simulation history

if "history" not in st.session_state:

    st.session_state.history = []


# Initialize RAG only once

if "retriever" not in st.session_state:

    with st.spinner(
        "Loading RAG knowledge base..."
    ):

        st.session_state.retriever = (
            DocumentRetriever()
        )


# Initialize LLM only once

if "llm" not in st.session_state:

    st.session_state.llm = LLMClient()


# Retrieve objects

simulator = st.session_state.simulator
retriever = st.session_state.retriever
llm = st.session_state.llm

state = simulator.get_state()


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header(
    "🎮 Simulation Controls"
)


# --------------------------------------------------
# Run Simulation
# --------------------------------------------------

if st.sidebar.button(
    "▶️ Run Simulation Step",
    use_container_width=True
):

    simulator.update()

    state = simulator.get_state()

    # Save current state

    st.session_state.history.append({

        "Step": simulator.step_count,

        "Altitude (ft)": state.altitude,

        "Speed (kt)": state.speed,

        "Fuel (%)": state.fuel,

        "Heading (°)": state.heading,

        "Weather": state.weather,

        "Communication": state.communication,

        "Navigation": state.navigation

    })

    st.rerun()


# --------------------------------------------------
# Reset Simulation
# --------------------------------------------------

if st.sidebar.button(
    "🔄 Reset Simulation",
    use_container_width=True
):

    aircraft = normal_scenario()

    st.session_state.simulator = FlightSimulator(
        aircraft
    )

    st.session_state.history = []

    st.rerun()


# --------------------------------------------------
# Simulation Information
# --------------------------------------------------

st.sidebar.divider()

st.sidebar.write(
    f"Simulation Step: "
    f"**{simulator.step_count}**"
)

st.sidebar.write(
    f"History Records: "
    f"**{len(st.session_state.history)}**"
)


# ==================================================
# AIRCRAFT STATE
# ==================================================

st.header(
    f"✈️ Aircraft {state.aircraft_id}"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Altitude",
        f"{state.altitude:.0f} ft"
    )


with col2:

    st.metric(
        "Speed",
        f"{state.speed:.0f} kt"
    )


with col3:

    st.metric(
        "Fuel",
        f"{state.fuel:.1f}%"
    )


with col4:

    st.metric(
        "Heading",
        f"{state.heading:.0f}°"
    )


st.divider()


# ==================================================
# SYSTEM STATUS
# ==================================================

st.subheader(
    "🛰️ Aircraft Systems"
)


col1, col2, col3 = st.columns(3)


# --------------------------------------------------
# Weather
# --------------------------------------------------

with col1:

    st.write("🌦️ Weather")

    if state.weather == "Clear":

        st.success(
            state.weather
        )

    else:

        st.warning(
            state.weather
        )


# --------------------------------------------------
# Communication
# --------------------------------------------------

with col2:

    st.write("📡 Communication")

    if state.communication == "Normal":

        st.success(
            state.communication
        )

    else:

        st.warning(
            state.communication
        )


# --------------------------------------------------
# Navigation
# --------------------------------------------------

with col3:

    st.write("🧭 Navigation")

    if state.navigation == "Normal":

        st.success(
            state.navigation
        )

    else:

        st.warning(
            state.navigation
        )


st.divider()


# ==================================================
# POSITION
# ==================================================

st.subheader(
    "📍 Simulated Aircraft Position"
)


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Latitude",
        f"{state.latitude:.4f}"
    )


with col2:

    st.metric(
        "Longitude",
        f"{state.longitude:.4f}"
    )


st.divider()


# ==================================================
# SIMULATION HISTORY
# ==================================================

st.subheader(
    "📊 Simulation History"
)


if st.session_state.history:

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "Run simulation steps to generate history."
    )


st.divider()


# ==================================================
# SIMULATION CHARTS
# ==================================================

if st.session_state.history:

    st.subheader(
        "📈 Flight Simulation Trends"
    )

    history_df = pd.DataFrame(
        st.session_state.history
    )

    # ----------------------------------------------
    # ALTITUDE + SPEED
    # ----------------------------------------------

    col1, col2 = st.columns(2)

    # ----------------------------------------------
    # Altitude Chart
    # ----------------------------------------------

    with col1:

        st.write("🛫 Altitude")

        altitude_chart = history_df[
            ["Step", "Altitude (ft)"]
        ].set_index("Step")

        st.line_chart(
            altitude_chart,
            height=280,
            use_container_width=True
        )

    # ----------------------------------------------
    # Speed Chart
    # ----------------------------------------------

    with col2:

        st.write("💨 Speed")

        speed_chart = history_df[
            ["Step", "Speed (kt)"]
        ].set_index("Step")

        st.line_chart(
            speed_chart,
            height=280,
            use_container_width=True
        )

    # ----------------------------------------------
    # Fuel Chart
    # ----------------------------------------------

    st.write("⛽ Fuel Level")

    fuel_chart = history_df[
        ["Step", "Fuel (%)"]
    ].set_index("Step")

    st.line_chart(
        fuel_chart,
        height=280,
        use_container_width=True
    )

else:

    st.info(
        "Run simulation steps to generate flight trends."
    )


st.divider()


# ==================================================
# AI ANALYSIS
# ==================================================

st.subheader(
    "🧠 AI State Analysis"
)


alerts = analyze_state(
    state
)


if alerts:

    for alert in alerts:

        st.warning(
            f"⚠️ {alert}"
        )

else:

    st.success(
        "No active alerts detected."
    )


st.divider()


# ==================================================
# RAG QUERY
# ==================================================

st.subheader(
    "🔎 RAG Query"
)


query = build_rag_query(
    state
)


st.code(
    query,
    language="text"
)


st.divider()


# ==================================================
# RETRIEVAL
# ==================================================

st.subheader(
    "📚 Retrieved Knowledge"
)


results = retriever.search(
    query,
    top_k=2
)


if results:

    for result in results:

        with st.expander(
            f"📄 {result['filename']}"
        ):

            st.write(
                result["text"]
            )

else:

    st.info(
        "No relevant simulated knowledge found."
    )


st.divider()


# ==================================================
# AI SITUATION REPORT
# ==================================================

st.subheader(
    "🤖 AI Situation Report"
)


with st.spinner(
    "Generating grounded AI report..."
):

    report = llm.generate_report(

        aircraft_state=state,

        alerts=alerts,

        knowledge=results

    )


st.markdown(
    report
)


st.divider()


# ==================================================
# FOOTER
# ==================================================

st.caption(
    "AeroMind — Simulated AI Aviation Training Environment"
)