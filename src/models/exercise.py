from dataclasses import dataclass


@dataclass
class Exercise:
    date: str
    exercise_name: str
    category: str
    duration: int
    calories_burned: int
    distance: float
    sets: int
    reps: int