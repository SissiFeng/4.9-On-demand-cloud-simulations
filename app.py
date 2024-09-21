from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# TODO: Load the trained model
# model = joblib.load('material_property_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # TODO: Get input data from request
    # data = request.json
    
    # TODO: Make prediction
    # prediction = model.predict([[data['feature1'], data['feature2'], data['feature3']]])
    
    # TODO: Return prediction as JSON
    # return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
