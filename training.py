import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import joblib

# ===============================
# Load dataset
# ===============================
df = pd.read_excel(r"K:\ML\Random Forest\Random Forest Regression\realistic_housing_data.xlsx")

# ===============================
# Define features and target
# ===============================
numeric_features = [
    'bedrooms', 'bathrooms', 'sqft', 'lot_size', 'age', 
    'year_built', 'garage', 'school_rating', 
    'has_pool', 'has_fireplace', 'has_basement'
]

categorical_features = ['location', 'house_type', 'condition']

features = numeric_features + categorical_features
target = 'price'

X = df[features]
y = df[target]

# ===============================
# Build preprocessor
# ===============================
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# ===============================
# Build pipeline
# ===============================
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# ===============================
# Train pipeline
# ===============================
pipeline.fit(X, y)

# ===============================
# Save the pipeline
# ===============================
joblib.dump(pipeline, "pipeline.pkl")
print("✅ Model pipeline saved successfully as 'pipeline.pkl'")
