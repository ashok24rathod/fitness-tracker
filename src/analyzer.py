import pandas as pd

class WorkoutAnalyzer:

    def __init__(self, df):
        self.df = df.copy()

        self.df["Volume"] = (
            self.df["Sets"]
            * self.df["Reps"]
            * self.df["Weight"]
        )

        self.df["Estimated1RM"] = (
            self.df["Weight"]
            * (1 + self.df["Reps"] / 30)
        )

    def total_volume(self):
        return self.df["Volume"].sum()

    def exercise_summary(self):
        return self.df.groupby("Exercise").agg(
            Sessions=("Exercise", "count"),
            TotalVolume=("Volume", "sum"),
            AvgWeight=("Weight", "mean"),
            PR=("Weight", "max")
        )

    def monthly_volume(self):
        monthly = self.df.groupby(
            self.df["Date"].dt.to_period("M")
        )["Volume"].sum()

        return monthly

    def personal_records(self):
        return self.df.groupby("Exercise")["Weight"].max()

    def exercise_frequency(self):
        return self.df["Exercise"].value_counts()

    def one_rm_progress(self, exercise):

        exercise_df = self.df[
            self.df["Exercise"] == exercise
        ]

        return exercise_df[
            ["Date", "Estimated1RM"]
        ].sort_values("Date")