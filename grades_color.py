import pandas as pd

students = {"name": ["Tim Voss", "Nicole Johnson", "Elsa Williams", "John James", "Catherine Jones"], "age": [19, 20, 21, 20, 23], "favorite_color": ["red", "yellow", "green", "blue", "green"], "grade": [91, 95, 82, 75, 93]}

students_df = pd.DataFrame(students)

def grades_colors(students_df: pd.DataFrame):
    students_df = students_df[(students_df["grade"] > 90) &
        students_df["favorite_color"].isin(["red", "green"])]
    return students_df

end_list = grades_colors(students_df)

print(end_list)