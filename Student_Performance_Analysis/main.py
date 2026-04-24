from source.preprocess import load_data, inspect_data, clean_data, feature_engineering
from source.analysis import *

def main():
    path = r"C:/Users/sankalp pandey/OneDrive/Documents/Student_Performance_Analysis/data/student_dataset_v2.csv"

    df = load_data(path)

    inspect_data(df)

    df = clean_data(df)

    df = feature_engineering(df)

    # Analysis
    top_students(df)
    low_performers(df)

    study_vs_marks(df)
    attendance_vs_marks(df)

    group_analysis(df)


if __name__ == "__main__":
    main()