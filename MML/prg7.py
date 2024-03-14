from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Example dataset with patients having and not having cancer
# X contains features (e.g., medical history, test results)
# y contains labels (0 for no cancer, 1 for cancer)

# Features for patients with cancer
X_cancer = [[1, 0, 0.2], [1, 1, 0.5], [1, 0, 0.8], [0, 1, 0.4]]  

# Features for patients without cancer
X_no_cancer = [[0, 1, 0.2], [1, 0, 0.5], [0, 0, 0.8], [1, 1, 0.4]]  

# Combine both sets of features
X = X_cancer + X_no_cancer  

# Labels for patients with cancer (1)
y_cancer = [1, 1, 1, 1]

# Labels for patients without cancer (0)
y_no_cancer = [0, 0, 0, 0]

# Combine both sets of labels
y = y_cancer + y_no_cancer  

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize SVM classifier
classifier = SVC(kernel='linear')

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Example usage of the classifier
# Replace test_patient with actual patient data
test_patient = [[0, 1, 0.2]]  # Example test data
prediction = classifier.predict(test_patient)
if prediction[0] == 0:
    print("The patient does not have cancer.")
else:
    print("The patient has cancer.")