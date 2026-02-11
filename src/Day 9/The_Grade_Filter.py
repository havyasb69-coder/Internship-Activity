import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

missing = grades.isnull()

filled_grades = grades.fillna(0)
filtered = filled_grades[filled_grades > 60]


print("Original Series:")
print(grades)

print("\nMissing values (True = missing):")
print(missing)

print("\nFilled Series:")
print(filled_grades)

print("\nScores greater than 60:")
print(filtered)
