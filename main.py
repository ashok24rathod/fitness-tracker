from src.loader import (
    load_workouts,
    load_bodyweight
)

from src.analyzer import WorkoutAnalyzer
from src.visualizer import Visualizer
from src.insights import InsightEngine

def main():

    workouts = load_workouts(
        "data/workouts.csv"
    )

    bodyweight = load_bodyweight(
        "data/bodyweight.csv"
    )

    analyzer = WorkoutAnalyzer(workouts)

    InsightEngine.generate_summary(analyzer)

    print("\nExercise Summary\n")
    print(analyzer.exercise_summary())

    monthly = analyzer.monthly_volume()

    Visualizer.plot_monthly_volume(monthly)

    exercise = "Bench Press"

    progress = analyzer.one_rm_progress(exercise)

    print(
        "\nPlateau Analysis:",
        InsightEngine.detect_plateau(progress)
    )

    Visualizer.plot_1rm(
        progress,
        exercise
    )

if __name__ == "__main__":
    main()