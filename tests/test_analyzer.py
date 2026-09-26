from app.simulator.scenarios import degraded_scenario
from app.simulator.state_analyzer import analyze_state


aircraft = degraded_scenario()

alerts = analyze_state(aircraft)

print("Current situation:")

for alert in alerts:
    print(f"- {alert}")