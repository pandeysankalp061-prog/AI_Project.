
import matplotlib.pyplot as plt
import seaborn as sns

def top_students(df):
    print("\nTop 5 Students:")
    print(df.sort_values(by='Marks', ascending=False).head())


def low_performers(df):
    print("\nStudents with Marks < 50:")
    print(df[df['Marks'] < 50])


def study_vs_marks(df):
    plt.figure()
    sns.scatterplot(x=df['StudyHours'], y=df['Marks'])
    plt.title("Study Hours vs Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.show()


def attendance_vs_marks(df):
    plt.figure()
    sns.scatterplot(x=df['Attendance'], y=df['Marks'])
    plt.title("Attendance vs Marks")
    plt.xlabel("Attendance")
    plt.ylabel("Marks")
    plt.show()


def group_analysis(df):
    print("\nAverage Marks by Attendance:")
    print(df.groupby('Attendance')['Marks'].mean())

    def study_category(hours):
        if hours < 3:
            return "Low"
        elif hours < 7:
            return "Medium"
        else:
            return "High"

    df['StudyCategory'] = df['StudyHours'].apply(study_category)

    print("\nAverage Marks by Study Category:")
    print(df.groupby('StudyCategory')['Marks'].mean())