import sqlite3
import pandas as pd

conn = sqlite3.connect("C:/SQLite/internship.db")

df = pd.read_sql_query("SELECT * FROM interns", conn)
print(f"All data Retrieved:\n{df}")

gt5000 = pd.read_sql_query(
    "SELECT * FROM interns WHERE track='Data Science' AND stipend > 5000;",
    conn
)
print(f"\nData Science interns with Greater than 5000 stipend:\n{gt5000}")

gp_track = pd.read_sql_query(
    "SELECT track, AVG(stipend) AS Average_Stipend FROM interns GROUP BY track;",
    conn
)
print(f"\nAverage Stipend for each track:\n{gp_track}")

cnt_track = pd.read_sql_query(
    "SELECT track, COUNT(*) AS intern_count FROM interns GROUP BY track;",
    conn
)
print(f"\nCount of Employees / Interns for each track:\n{cnt_track}")

conn.close()