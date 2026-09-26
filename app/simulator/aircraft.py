from pydantic import BaseModel


class AircraftState(BaseModel):
    aircraft_id: str
    altitude: float
    speed: float
    heading: float
    fuel: float

    weather: str
    communication: str
    navigation: str

    latitude: float
    longitude: float