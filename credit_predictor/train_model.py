import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.DataFrame({
    'idade': [25, 40, 30, 50, 22],
    'renda': [3000, 7000, 4000, 10000, 2500],
    'divida': [500, 2000, 1500, 3000, 1000],
    'inadimplente': [0, 1, 0, 1, 0]
})

X = data[['idade', 'renda', 'divida']]
y = data['inadimplente']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'model.pkl')