import matplotlib.pyplot as plt

class Visualizer:

    @staticmethod
    def plot_monthly_volume(monthly_data):

        monthly_data.plot(
            kind="bar",
            figsize=(8, 4),
            color="skyblue"
        )

        plt.title("Monthly Training Volume")
        plt.ylabel("Volume")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_1rm(progress_df, exercise):

        plt.figure(figsize=(8, 4))

        plt.plot(
            progress_df["Date"],
            progress_df["Estimated1RM"],
            marker="o"
        )

        plt.title(f"{exercise} Estimated 1RM")
        plt.ylabel("1RM")
        plt.grid(True)
        plt.tight_layout()
        plt.show()