import pandas as pd
import mysql.connector
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '@MYsql23!',
    'database': 'Food',
}
connection = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)

if connection.is_connected():
    print("Connected to MySQL database")

query = 'SELECT * FROM Surplus'  # Modify the SQL query according to your table structure
data = pd.read_sql(query, con=connection)

# Define a threshold to classify 'waste_in_grams' as High or Low
val=pd.Series(data['waste_in_grams']).median()
threshold = np.percentile(data['waste_in_grams'],val)

data['waste_category'] = np.where(data['waste_in_grams'] > threshold, 'High', 'Low')
# Select and encode the relevant features
selected_features = ['quantity_in_grams', 'ingredient_count','food_type']
X = data[selected_features]
X = pd.get_dummies(X, columns=['food_type'])  # Encode the 'food_type' feature

y = data['waste_category']
X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=42)

# Train a classifier (e.g., Random Forest) using the selected features
clf = RandomForestClassifier(max_depth=3, min_samples_split=2, min_samples_leaf=1, n_estimators=60,random_state=46)
kf = KFold(n_splits=5, shuffle=True, random_state=42)  # You can adjust the number of folds (n_splits)
cross_val_scores = cross_val_score(clf, X, y, cv=kf)

# Print the cross-validated scores



# Fit the model on the entire dataset
clf.fit(X, y)


# Evaluate the model on the validation set
y_pred = clf.predict(X_valid)
accuracy = accuracy_score(y_valid, y_pred)
# print(f"Model Accuracy: {accuracy:.2f}")
report = classification_report(y_valid, y_pred, target_names=['Low', 'High'])
# print("Classification Report:")
# print(report)
def check_overfitting(clf, X, y, X_valid, y_valid, cv):
    # Calculate cross-validated scores
    cross_val_scores = cross_val_score(clf, X, y, cv=cv)

    # Fit the model on the entire dataset
    clf.fit(X, y)

    # Evaluate the model on the validation set
    y_pred = clf.predict(X_valid)
    accuracy = accuracy_score(y_valid, y_pred)

    # Calculate the mean and standard deviation of cross-validated scores
    mean_cv_score = cross_val_scores.mean()
    std_cv_score = cross_val_scores.std()

    # Compare cross-validated scores to the validation set accuracy
    print(f"Mean Cross-Validated Score: {mean_cv_score:.2f}")
    print(f"Standard Deviation of Cross-Validated Scores: {std_cv_score:.2f}")
    print(f"Validation Set Accuracy: {accuracy:.2f}")

    # Check if overfitting might be occurring
    if mean_cv_score > accuracy:
        print("Warning: The model may be overfitting to the training data.")
    else:
        print("The model does not appear to be overfitting.")




