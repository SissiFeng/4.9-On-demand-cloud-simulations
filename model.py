import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def create_mock_data():
    np.random.seed(42)
    n_samples = 1000

    data = pd.DataFrame({
        'composition_A': np.random.uniform(0, 1, n_samples),
        'composition_B': np.random.uniform(0, 1, n_samples),
        'processing_temp': np.random.uniform(500, 1500, n_samples),
        'processing_time': np.random.uniform(1, 10, n_samples),
        'hardness': np.random.uniform(100, 1000, n_samples)
    })

    data['hardness'] += (data['composition_A'] * 200 + 
                         data['composition_B'] * 100 + 
                         data['processing_temp'] * 0.1 + 
                         data['processing_time'] * 10)

    data.to_csv('materials_data.csv', index=False)
    return data

def train_model(data):
    # TODO: Prepare features (X) and target (y)
    # Hint: Select appropriate columns for X and y

    # TODO: Split the data into training and testing sets
    # Hint: Use train_test_split function

    # TODO: Create and train the model
    # Hint: Initialize RandomForestRegressor and use its fit method

    # TODO: Evaluate the model
    # Hint: Use the model to predict on X_test and calculate mean squared error

    # TODO: Save the model
    # Hint: Use joblib.dump()

    return model, mse

def test_model():
    # Load the saved model
    loaded_model = joblib.load('material_property_model.joblib')

    # Create a small test dataset
    test_data = pd.DataFrame({
        'composition_A': [0.5, 0.3, 0.7],
        'composition_B': [0.5, 0.7, 0.3],
        'processing_temp': [1000, 800, 1200],
        'processing_time': [5, 3, 7]
    })

    # Make predictions
    predictions = loaded_model.predict(test_data)

    # Check if predictions are within a reasonable range
    assert all(100 <= pred <= 1500 for pred in predictions), "Predictions out of expected range"

    print("Model test passed successfully!")

if __name__ == "__main__":
    data = create_mock_data()
    model, mse = train_model(data)
    print(f"Mean Squared Error: {mse}")
    print("Model training completed and saved.")
    
    # Run the test
    test_model()
