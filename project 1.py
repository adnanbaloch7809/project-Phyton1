import pandas as pd

class Student:
    def __init__(self, name, math_score, science_score):
        self.name = name
        self.math_score = math_score
        self.science_score = science_score
        self.status = None

    def check_status(self):
        avg = (self.math_score + self.science_score) / 2
        if avg >= 50:
            self.status = "Pass"
        else:
            self.status = "Fail"


df = pd.read_csv("raw_grades.csv")

df = df.fillna(0)

print("\nCleaned Data:")
print(df)

students_list = []

for index, row in df.iterrows():
    student = Student(
        row["Student_Name"],
        row["Math_Score"],
        row["Science_Score"]
    )

    student.check_status()

    students_list.append({
        "Student_Name": student.name,
        "Math_Score": student.math_score,
        "Science_Score": student.science_score,
        "Status": student.status
    })

final_df = pd.DataFrame(students_list)

final_df["School_Year"] = "2023-2024"

final_df.to_csv("final_grades.csv", index=False)

print("\nFinal Report:")
print(final_df)

print("\nSaved as final_grades.csv")