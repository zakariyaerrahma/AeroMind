from app.simulator.scenarios import normal_scenario
from app.simulator.engine import FlightSimulator


aircraft = normal_scenario()
simulator = FlightSimulator(aircraft)


for step in range(10):

    state = simulator.update()

    print(
        f"Step {step + 1}: "
        f"Altitude={state.altitude} ft | "
        f"Speed={state.speed} kt | "
        f"Fuel={state.fuel:.1f}%"
    )