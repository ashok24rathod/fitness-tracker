from dataclasses import dataclass


@dataclass
class Measurement:
    date: str
    weight: float
    height: float
    waist: float
    chest: float
    hips: float
    body_fat: float