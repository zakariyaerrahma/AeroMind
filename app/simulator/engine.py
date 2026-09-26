from .aircraft import AircraftState


class FlightSimulator:

    def __init__(self, aircraft: AircraftState):

        self.aircraft = aircraft

        # Number of simulation steps
        self.step_count = 0

    def update(self):

        # Increase simulation step
        self.step_count += 1

        # --------------------------------
        # Fuel consumption
        # --------------------------------

        self.aircraft.fuel = max(
            0,
            self.aircraft.fuel - 0.5
        )

        # --------------------------------
        # Flight movement
        # --------------------------------

        self.aircraft.altitude += 100

        self.aircraft.speed -= 2

        self.aircraft.latitude += 0.001

        self.aircraft.longitude += 0.001

        # --------------------------------
        # Simulation events
        # --------------------------------

        if self.step_count == 5:

            self.aircraft.weather = "Severe"

        if self.step_count == 8:

            self.aircraft.communication = "Degraded"

        if self.step_count == 10:

            self.aircraft.navigation = "Degraded"

        return self.aircraft

    def get_state(self):

        return self.aircraft