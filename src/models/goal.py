from dataclasses import dataclass


@dataclass
class Goal:
    goal_type: str
    start_weight: float
    target_weight: float
    target_date: str