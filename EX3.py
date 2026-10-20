import pandas as pd
import numpy as np
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer, Binarizer, LabelEncoder

csv_data = """Age,Income,SpendingScore,LoyaltyIndex,Gender,Purchased
25,50000,80,0.9,Male,No
45,100000,20,0.5,Female,Yes
35,75000,60,0.8,Female,No
50,120000,10,0.3,Male,Yes
20,30000,90,0.95,Male,No
55,110000,15,0.4,Female,Yes"""

df = pd.read_csv(StringIO(csv_data))

print("--- Original DataFrame ---")
print(df)
print("-" * 30)

le = LabelEncoder()

df['Purchased_Label'] = le.fit_transform(df['Purchased'])

df['Gender_Label'] = le.fit_transform(df['Gender'])

print("\n--- After Label Encoding ---")
print(df[['Gender', 'Gender_Label', 'Purchased', 'Purchased_Label']].head())

X = df[['Age', 'Income', 'SpendingScore', 'LoyaltyIndex']]
y = df['Purchased_Label']

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.3,    
    random_state=42   
)

print("-" * 30)
print(f"Train set size: {X_train.shape[0]} samples")
print(f"Test set size:  {X_test.shape[0]} samples")

scaler_std = StandardScaler()

X_train_std = scaler_std.fit_transform(X_train)
X_test_std = scaler_std.transform(X_test)

scaler_minmax = MinMaxScaler()
X_train_minmax = scaler_minmax.fit_transform(X_train)
X_test_minmax = scaler_minmax.transform(X_test)

normalizer = Normalizer()
X_train_l2 = normalizer.fit_transform(X_train)

binarizer = Binarizer(threshold=80000)
income_binary_train = binarizer.fit_transform(X_train[['Income']])

print("\n--- Preprocessing Results (First row of Train Set) ---")
print(f"Standardized Age: {X_train_std[0][0]:.4f}")
print(f"MinMax Scaled Age: {X_train_minmax[0][0]:.4f}")
print(f"L2 Normalized Age: {X_train_l2[0][0]:.4f}")
print(f"Binarized Income: {income_binary_train[0][0]}")