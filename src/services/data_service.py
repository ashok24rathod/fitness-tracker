import os
import pandas as pd


class DataService:

    DATA_DIR = "data"

    PROFILE_FILE = os.path.join(DATA_DIR, "profile.csv")
    MEASUREMENTS_FILE = os.path.join(DATA_DIR, "body_measurements.csv")
    EXERCISE_FILE = os.path.join(DATA_DIR, "exercises.csv")
    GOAL_FILE = os.path.join(DATA_DIR, "goals.csv")

    @staticmethod
    def initialize_files():

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(DataService.PROFILE_FILE):
            pd.DataFrame(columns=[
                "name",
                "age",
                "gender",
                "height"
            ]).to_csv(DataService.PROFILE_FILE, index=False)

        if not os.path.exists(DataService.MEASUREMENTS_FILE):
            pd.DataFrame(columns=[
                "date",
                "weight",
                "height",
                "waist",
                "chest",
                "hips",
                "body_fat"
            ]).to_csv(DataService.MEASUREMENTS_FILE, index=False)

        if not os.path.exists(DataService.EXERCISE_FILE):
            pd.DataFrame(columns=[
                "date",
                "exercise_name",
                "category",
                "duration",
                "calories_burned",
                "distance",
                "sets",
                "reps"
            ]).to_csv(DataService.EXERCISE_FILE, index=False)

        if not os.path.exists(DataService.GOAL_FILE):
            pd.DataFrame(columns=[
                "goal_type",
                "start_weight",
                "target_weight",
                "target_date"
            ]).to_csv(DataService.GOAL_FILE, index=False)

    # ------------------------
    # Profile
    # ------------------------

    @staticmethod
    def save_profile(profile):

        pd.DataFrame([profile]).to_csv(
            DataService.PROFILE_FILE,
            index=False
        )

    @staticmethod
    def get_profile():

        df = pd.read_csv(DataService.PROFILE_FILE)

        if df.empty:
            return None

        return df.iloc[0].to_dict()

    # ------------------------
    # Measurements
    # ------------------------

    @staticmethod
    def add_measurement(data):

        df = pd.read_csv(DataService.MEASUREMENTS_FILE)

        df.loc[len(df)] = data

        df.to_csv(
            DataService.MEASUREMENTS_FILE,
            index=False
        )

    @staticmethod
    def get_measurements():

        return pd.read_csv(
            DataService.MEASUREMENTS_FILE
        )

    # ------------------------
    # Exercises
    # ------------------------

    @staticmethod
    def add_exercise(data):

        df = pd.read_csv(
            DataService.EXERCISE_FILE
        )

        df.loc[len(df)] = data

        df.to_csv(
            DataService.EXERCISE_FILE,
            index=False
        )

    @staticmethod
    def get_exercises():

        return pd.read_csv(
            DataService.EXERCISE_FILE
        )

    # ------------------------
    # Goals
    # ------------------------

    @staticmethod
    def save_goal(goal):

        pd.DataFrame([goal]).to_csv(
            DataService.GOAL_FILE,
            index=False
        )

    @staticmethod
    def get_goal():

        df = pd.read_csv(
            DataService.GOAL_FILE
        )

        if df.empty:
            return None

        return df.iloc[0].to_dict()