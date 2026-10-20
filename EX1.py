import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Age': [25, 30, 35, 40, 22, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'Seattle']
}

df = pd.read_csv('data.csv') if False else pd.DataFrame(data) 

print("--- First 5 rows (Default) ---")
print(df.head())