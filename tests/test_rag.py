from app.simulator.scenarios import degraded_scenario

from app.simulator.state_analyzer import (
    analyze_state,
    build_rag_query
)

from app.rag.retriever import DocumentRetriever

from app.llm.client import LLMClient


# -----------------------------
# Aircraft
# -----------------------------

aircraft = degraded_scenario()


print("\n=== AIRCRAFT STATE ===")

print(f"Aircraft: {aircraft.aircraft_id}")
print(f"Altitude: {aircraft.altitude} ft")
print(f"Speed: {aircraft.speed} kt")
print(f"Fuel: {aircraft.fuel}%")
print(f"Weather: {aircraft.weather}")
print(f"Communication: {aircraft.communication}")
print(f"Navigation: {aircraft.navigation}")


# -----------------------------
# State Analysis
# -----------------------------

alerts = analyze_state(aircraft)


print("\n=== AI ANALYSIS ===")

for alert in alerts:

    print(f"- {alert}")


# -----------------------------
# RAG
# -----------------------------

query = build_rag_query(aircraft)


print("\n=== RAG QUERY ===")

print(query)


retriever = DocumentRetriever()


results = retriever.search(
    query,
    top_k=2
)


print("\n=== RETRIEVED KNOWLEDGE ===")


for result in results:

    print("=" * 50)

    print(result["filename"])


# -----------------------------
# LLM
# -----------------------------

llm = LLMClient()


report = llm.generate_report(
    aircraft_state=aircraft,
    alerts=alerts,
    knowledge=results
)


print("\n=== AI SITUATION REPORT ===\n")

print(report)