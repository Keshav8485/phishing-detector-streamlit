import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Step 1: Load dataset
df = pd.read_csv(r"C:\Users\91964\OneDrive\Desktop\PhiUSIIL_Phishing_URL_Dataset.csv")

# Step 2: Drop non-feature columns (like FILENAME, URL, TLD, Title, etc.)
columns_to_drop = ['FILENAME', 'URL', 'Domain', 'TLD', 'Title', 'Robots']  # drop columns that are not numeric
df = df.drop(columns=columns_to_drop)

# Step 3: Split into features (X) and label (y)
X = df.drop('label', axis=1)
y = df['label']

# Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 6: Save model
joblib.dump(model, "phishing_model.pkl")
print("✅ Model trained and saved as phishing_model.pkl")
