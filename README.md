# Cloud Deployment of Materials Discovery Model

## 🎯 Assignment Overview

In this assignment, you will develop a machine learning model for materials discovery, create web interfaces for it, and deploy the model to various cloud platforms. This project will give you hands-on experience with model development, API creation, containerization, and cloud deployment.

## 🚀 Assignment Steps

### 1. Model Development

#### 1.1 Complete the `model.py` file
- Open `model.py`
- Implement the following TODO sections:
  - Prepare features (X) and target (y)
  - Split the data into training and testing sets
  - Create and train the model
  - Evaluate the model
  - Save the model
- Run the script to train and save your model:
  ```
  python model.py
  ```

#### 1.2 Verify your implementation
- Run the check script:
  ```
  python check_submission.py
  ```
- Ensure all checks pass. If not, revisit your implementation and make necessary corrections.

### 2. Flask API Development

#### 2.1 Complete the `app.py` file
- Open `app.py`
- Implement the following TODO sections:
  - Load the trained model
  - Get input data from request
  - Make prediction
  - Return prediction as JSON
- Test your Flask app locally:
  ```
  python app.py
  ```
- Use a tool like curl or Postman to test the `/predict` endpoint

### 3. Gradio Interface Development

#### 3.1 Complete the `gradio_app.py` file
- Open `gradio_app.py`
- Implement the following TODO sections:
  - Load the trained model
  - Create the prediction function
  - Set up the Gradio interface
- Test your Gradio app locally:
  ```
  python gradio_app.py
  ```

### 4. Containerization

#### 4.1 Complete the `Dockerfile`
- Open `Dockerfile`
- Fill in the TODO sections:
  - Choose a base image
  - Set working directory
  - Copy requirements file and install dependencies
  - Copy application files
  - Set environment variables (if needed)
  - Expose port
  - Set the command to run the application
- Build and test your Docker image locally:
  ```
  docker build -t materials-discovery-app .
  docker run -p 5000:5000 materials-discovery-app
  ```

### 5. Prepare requirements.txt

#### 5.1 Update requirements.txt
- Open `requirements.txt`
- Ensure it includes all necessary libraries for your project. At minimum, it should contain:
  ```
  Flask==2.0.1
  scikit-learn==0.24.2
  pandas==1.3.3
  joblib==1.0.1
  gradio==2.0.8
  ```
- Add any other libraries you've used in your project
- Save the file

### 6. Cloud Deployments

#### 6.1 PythonAnywhere Deployment
- Sign up for a free PythonAnywhere account
- Upload your `app.py`, trained model file, and `requirements.txt`
- Create a new virtual environment and install the requirements:
  ```
  mkvirtualenv --python=/usr/bin/python3.8 myenv
  pip install -r requirements.txt
  ```
- Set up a new Web app using Flask
- Configure your app and make sure it's running
- Test your deployed app and save the URL

#### 6.2 Hugging Face Spaces Deployment
- Sign up for a Hugging Face account
- Create a new Space, choosing Gradio as the SDK
- Upload your `gradio_app.py`, trained model file, and `requirements.txt`
- Hugging Face will automatically install the requirements from your `requirements.txt`
- Ensure your app is running correctly on Hugging Face Spaces
- Save the deployment URL

#### 6.3 Google Cloud Run Deployment
- Set up a Google Cloud account (using free credits)
- Install and configure Google Cloud SDK
- Ensure your `Dockerfile` copies and uses the `requirements.txt`:
  ```dockerfile
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  ```
- Build your Docker image and push it to Google Container Registry
- Deploy your app using Google Cloud Run
- Test your deployed app and save the URL

### 7. Documentation and Comparison

#### 7.1 Update existing README.md
- Open the existing `README.md` file in the root of your repository
- Keep the original content at the top that describes the assignment
- Add a new section at the bottom of the file with the following information:
  - Brief description of your implemented model and its purpose
  - PythonAnywhere deployment URL
  - Hugging Face Spaces deployment URL
  - Google Cloud Run deployment URL
- Save the updated README.md file
   
Example structure for your additions:

```
My Implementation
Model Description
[Your model description here]
Deployment URLs
PythonAnywhere: [Your URL here]
Hugging Face Spaces: [Your URL here]
Google Cloud Run: [Your URL here]
Deployment Comparison
[Your comparison and analysis here]
```

   
  
### 8. Final Submission

#### 8.1 Push your changes to GitHub
- Commit all your changes:
  ```
  git add .
  git commit -m "Complete cloud deployment assignment"
  git push origin main
  ```
- This push will trigger the GitHub Actions workflow for autograding

#### 8.2 Verify autograding results
- Go to the "Actions" tab in your GitHub repository
- Check that all autograding checks have passed
- If any checks fail, review the error messages, make necessary corrections, and push again

## 📝 Grading Criteria

Your assignment will be graded based on:
- Correct implementation of the machine learning model
- Functionality of Flask API and Gradio interface
- Successful deployment to all three cloud platforms
- Completeness and quality of your README.md documentation
- Passing all autograding checks

Good luck with your cloud deployment project! 🍀
