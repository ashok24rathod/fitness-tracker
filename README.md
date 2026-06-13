# 🏋️ Fitness Tracker (Streamlit + CSV + Python)

A simple but powerful **personal fitness tracking application** built using Python and Streamlit.  
It helps you track **body measurements, workouts, and fitness goals**, and visualize your progress over time with charts and downloadable reports.

---

## 📌 Features

### 👤 Profile Management
- Save personal details (name, age, gender, height)

### 📏 Body Measurements Tracking
- Weight tracking over time
- Waist, chest, hips measurements
- Body fat percentage tracking

### 🏃 Exercise Logging
- Record workouts (running, cycling, gym, etc.)
- Track duration, calories burned, distance
- Track sets and reps for strength training

### 🎯 Goal Tracking
- Set weight loss or weight gain goals
- Define target weight and target date
- Monitor progress visually

### 📊 Analytics & Visualization
- Weight trend charts
- Exercise frequency analysis
- Calories burned trends
- Body measurement progress charts
- BMI calculation and tracking

### 📄 PDF Report Export
- Download complete fitness summary report
- Includes charts + stats + goals progress

---

## 🧱 Tech Stack

- Python 3.9+
- Streamlit (UI Dashboard)
- Pandas (Data handling)
- NumPy (Calculations)
- Matplotlib (Visualizations)
- Seaborn (Advanced charts)
- FPDF2 (PDF report generation)

---

## 📂 Project Structure

```text
fitness-tracker/
│
├── data/
│   ├── profile.csv
│   ├── body_measurements.csv
│   ├── exercises.csv
│   └── goals.csv
│
├── reports/
│
├── visualizations/
│
├── src/
│   ├── models/
│   ├── services/
│   └── utils/
│
├── dashboard.py
├── requirements.txt
└── README.md

TODO:
Need to add unit test cases and also wanted to load the data which is present in data folder when application startup occurs.
