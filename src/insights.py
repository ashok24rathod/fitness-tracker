class InsightEngine:

    @staticmethod
    def detect_plateau(df):

        if len(df) < 4:
            return "Not enough data."

        recent = df["Estimated1RM"].tail(4)

        change = recent.max() - recent.min()

        if change < 2:
            return (
                "Plateau detected. "
                "Strength has not improved significantly."
            )

        return "Progress is improving."

    @staticmethod
    def generate_summary(analyzer):

        print("\n===== FITNESS REPORT =====\n")

        print(
            f"Total Volume: "
            f"{analyzer.total_volume():,.0f}"
        )

        print("\nPersonal Records")
        print(analyzer.personal_records())

        print("\nExercise Frequency")
        print(analyzer.exercise_frequency())