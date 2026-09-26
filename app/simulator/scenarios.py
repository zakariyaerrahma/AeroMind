from .aircraft import AircraftState


def normal_scenario() -> AircraftState:
    return AircraftState(
        aircraft_id="A12",
        altitude=18000,
        speed=420,
        heading=270,
        fuel=75,
        weather="Clear",
        communication="Normal",
        navigation="Normal",
        latitude=30.4200,
        longitude=-9.6000,
    )


def severe_weather_scenario() -> AircraftState:
    return AircraftState(
        aircraft_id="A12",
        altitude=18000,
        speed=420,
        heading=270,
        fuel=55,
        weather="Severe",
        communication="Normal",
        navigation="Normal",
        latitude=30.4200,
        longitude=-9.6000,
    )


def degraded_scenario() -> AircraftState:
    return AircraftState(
        aircraft_id="A12",
        altitude=12000,
        speed=380,
        heading=250,
        fuel=25,
        weather="Severe",
        communication="Degraded",
        navigation="Degraded",
        latitude=30.4500,
        longitude=-9.5500,
    )