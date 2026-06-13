import streamlit as st

from src.services.data_service import DataService


st.set_page_config(
    page_title="Fitness Tracker",
    page_icon="🏋️",
    layout="wide"
)

DataService.initialize_files()

st.title("🏋️ Personal Fitness Tracker")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Profile",
        "Measurements",
        "Exercises",
        "Goals"
    ]
)

if menu == "Dashboard":

    st.header("Overview")

    st.info(
        "Welcome to your Fitness Tracker"
    )

elif menu == "Profile":

    st.header("Profile")

    with st.form("profile_form"):

        name = st.text_input("Name")
        age = st.number_input(
            "Age",
            1,
            100
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        height = st.number_input(
            "Height (cm)",
            50,
            250
        )

        submit = st.form_submit_button(
            "Save"
        )

        if submit:

            DataService.save_profile({
                "name": name,
                "age": age,
                "gender": gender,
                "height": height
            })

            st.success("Profile saved")

elif menu == "Measurements":

    st.header("Body Measurements")

    with st.form("measurement_form"):

        date = st.date_input("Date")

        weight = st.number_input(
            "Weight",
            min_value=0.0
        )

        height = st.number_input(
            "Height",
            min_value=0.0
        )

        waist = st.number_input(
            "Waist",
            min_value=0.0
        )

        chest = st.number_input(
            "Chest",
            min_value=0.0
        )

        hips = st.number_input(
            "Hips",
            min_value=0.0
        )

        body_fat = st.number_input(
            "Body Fat %",
            min_value=0.0
        )

        submit = st.form_submit_button(
            "Add Measurement"
        )

        if submit:

            DataService.add_measurement([
                str(date),
                weight,
                height,
                waist,
                chest,
                hips,
                body_fat
            ])

            st.success(
                "Measurement Added"
            )

elif menu == "Exercises":

    st.header("Exercise Tracker")

    with st.form("exercise_form"):

        date = st.date_input("Date")

        exercise = st.text_input(
            "Exercise Name"
        )

        category = st.selectbox(
            "Category",
            [
                "Cardio",
                "Strength",
                "Flexibility"
            ]
        )

        duration = st.number_input(
            "Duration (minutes)"
        )

        calories = st.number_input(
            "Calories Burned"
        )

        distance = st.number_input(
            "Distance (km)"
        )

        sets = st.number_input("Sets")

        reps = st.number_input("Reps")

        submit = st.form_submit_button(
            "Save Exercise"
        )

        if submit:

            DataService.add_exercise([
                str(date),
                exercise,
                category,
                duration,
                calories,
                distance,
                sets,
                reps
            ])

            st.success(
                "Exercise Added"
            )

elif menu == "Goals":

    st.header("Goal Tracking")

    with st.form("goal_form"):

        goal_type = st.selectbox(
            "Goal",
            [
                "Weight Loss",
                "Weight Gain"
            ]
        )

        start_weight = st.number_input(
            "Current Weight"
        )

        target_weight = st.number_input(
            "Target Weight"
        )

        target_date = st.date_input(
            "Target Date"
        )

        submit = st.form_submit_button(
            "Save Goal"
        )

        if submit:

            DataService.save_goal({
                "goal_type": goal_type,
                "start_weight": start_weight,
                "target_weight": target_weight,
                "target_date": str(target_date)
            })

            st.success("Goal Saved")