import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression

# Load dataset
digits = load_digits()
X = digits.data
y = digits.target

# Train model
model = LogisticRegression(max_iter=5000)
model.fit(X, y)

# Predict first 5 digits
predictions = model.predict(X[:5])

# Visualize 5 digits
plt.figure(figsize=(8,3))
for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(X[i].reshape(8,8), cmap='gray')
    plt.title("Pred: "+str(predictions[i]))
    plt.axis('off')

plt.show()