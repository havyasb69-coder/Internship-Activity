#Pandas Basics
import pandas as pd
s1 = pd.Series([10,20,30,40])
s2 = pd.Series([10,20,30],index=['a','b','c'])
print(s1)
print(s2)

#Indexing and Selection in Series
marks = pd.Series([85,90,78],index = ['Math','Physics','Chemistry'])
print(marks['Math'])
print(marks[['Math','Chemistry']])

#Boolean Masking in Series
scores = pd.Series([45, 67, 89, 34, 90])
passed = scores[scores > 60]
print("\n",passed,"\n")

#Handling missing values in Series
data = pd.Series([10, None, 30, None])
print(data.isnull())
print(data.fillna(0))
print(data.fillna("True"))

#Vectorized String Operations
names = pd.Series(['Alice', 'bob', 'CHARLIE'])
print("\n",names.str.lower())
print("\n",names .str.contains('a'))
print("\n",names.str.upper())
