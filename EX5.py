import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    'Horsepower': [100,120,150,180,200,220,250,270,300,320],
    'EngineSize': [1.2,1.4,1.6,1.8,2.0,2.2,2.5,2.7,3.0,3.2],
    'Price': [15000,18000,22000,26000,30000,35000,40000,45000,50000,55000]
}

df = pd.DataFrame(data)

df['Expensive'] = (df['Price'] > 30000).astype(int)

X = df[['Horsepower','EngineSize']]
y = df['Expensive']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test,predictions)
print("Model Accuracy:", accuracy)

new_car = np.array([[210,2.1]])
prediction = model.predict(new_car)

if prediction[0] == 1:
    print("The car is Expensive")
else:
    print("The car is Not Expensive")