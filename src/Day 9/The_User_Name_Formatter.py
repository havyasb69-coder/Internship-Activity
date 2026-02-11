import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned = usernames.str.strip().str.lower()
contains_a = cleaned.str.contains('a')
print(f"Original Usernames are : \n{usernames}" )

print("Cleaned usernames:")
print(cleaned)

print("\nContains letter 'a':")
print(contains_a)
