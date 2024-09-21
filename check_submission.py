import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

def check_model_file():
    assert os.path.exists('material_property_model.joblib'), "Model file not found"
    print("✅ Model file exists")

def check_data_loading():
    assert os.path.exists('materials_data.csv'), "Data file not found"
    data = pd.read_csv('materials_data.csv')
    assert len(data) == 1000, f"Expected 1000 samples, but found {len(data)}"
    assert set(data.columns) == {'composition_A', 'composition_B', 'processing_temp', 'processing_time', 'hardness'}, "Incorrect columns in the dataset"
    print("✅ Data loading check passed")

def check_model_performance():
    data = pd.read_csv('materials_data.csv')
    X = data[['composition_A', 'composition_B', 'processing_temp', 'processing_time']]
    y = data['hardness']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = joblib.load('material_property_model.joblib')
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    assert mse < 10000, f"Model performance is poor. MSE: {mse}"
    print(f"✅ Model performance check passed. MSE: {mse:.2f}")

def check_model_prediction():
    model = joblib.load('material_property_model.joblib')
    test_data = pd.DataFrame({
        'composition_A': [0.5, 0.3, 0.7],
        'composition_B': [0.5, 0.7, 0.3],
        'processing_temp': [1000, 800, 1200],
        'processing_time': [5, 3, 7]
    })
    predictions = model.predict(test_data)
    assert all(100 <= pred <= 1500 for pred in predictions), "Predictions out of expected range"
    print("✅ Model prediction check passed")

def main():
    try:
        check_model_file()
        check_data_loading()
        check_model_performance()
        check_model_prediction()
        print("\n🎉 All checks passed! Your submission looks good!")
    except AssertionError as e:
        print(f"\n❌ Check failed: {str(e)}")
        print("Please review your code and try again.")

if __name__ == "__main__":
    main()
