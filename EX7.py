from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

# Email dataset
emails = [
    "Win money now", 
    "Limited offer buy now",
    "Meeting at 10 am",
    "Project discussion tomorrow",
    "Congratulations you won a prize"
]

# Labels: 1 = Spam, 0 = Not Spam
labels = [1,1,0,0,1]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# Train SVM model
model = SVC()
model.fit(X, labels)

# Test email
test = ["Win a free ticket"]
test_vector = vectorizer.transform(test)

prediction = model.predict(test_vector)

print("Spam" if prediction[0]==1 else "Not Spam")