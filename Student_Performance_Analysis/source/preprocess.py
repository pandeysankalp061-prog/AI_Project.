import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df


def inspect_data(df):
    print("First 5 rows:\n", df.head())
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns)


def clean_data(df):
    print("\nMissing Values:\n", df.isnull().sum())

    df['Marks'].fillna(df['Marks'].mean(), inplace=True)
    df['StudyHours'].fillna(df['StudyHours'].median(), inplace=True)

    df = df[(df['StudyHours'] <= 15) & (df['Marks'] <= 100)]

    return df


def feature_engineering(df):
    def performance(marks):
        if marks >= 80:
            return "Excellent"
        elif marks >= 60:
            return "Good"
        else:
            return "Needs Improvement"

    df['Performance'] = df['Marks'].apply(performance)

    df['EffortScore'] = df['StudyHours'] * df['Attendance']

    return df