import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})

le = LabelEncoder()
data["Transmission"] = le.fit_transform(data["Transmission"])
data = pd.get_dummies(data, columns=["Color"], drop_first=True)

print(data)
