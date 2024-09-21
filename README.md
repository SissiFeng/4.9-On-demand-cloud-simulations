# On-Demand Cloud Simulations for Materials Discovery

## Project Overview
This project implements an on-demand cloud simulation system for materials discovery using AWS Lambda, Docker, and Prefect. It demonstrates the integration of machine learning models with cloud computing for efficient materials property prediction.

## Setup Instructions

### Prerequisites
- Python 3.8+
- AWS account with CLI configured
- Docker installed
- Prefect installed

### Installation
1. Clone this repository:
   ```
   git clone [repository-url]
   cd [repository-name]
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up AWS credentials:
   ```
   aws configure
   ```

## Assignment Steps

### 1. Implement the Simulator (simulator.py)
- Complete the `simulate_material_property` function in `simulator.py`.
- Run tests: `python test_simulation.py`

### 2. Develop AWS Lambda Function (lambda_function.py)
- Implement the `lambda_handler` function in `lambda_function.py`.
- Test locally: `python test_lambda_function.py`

### 3. Create Dockerfile
- Complete the Dockerfile for containerizing the Lambda function.

### 4. Implement Prefect Workflow (workflow.py)
- Open `workflow.py` and implement the following:
  - `generate_composition` task: Generate random material compositions.
  - `run_simulation` task: Call the AWS Lambda function to simulate material properties.
  - `analyze_result` task: Analyze the simulation results.
  - `material_discovery_workflow` flow: Orchestrate the entire workflow.
- Test locally:
  ```
  python workflow.py
  ```
### 5. Set up and Test Prefect
- Install Prefect if not already installed:
  ```
  pip install prefect
  ```
- Start the Prefect server (in a separate terminal):
  ```
  prefect server start
  ```
- In your main terminal, set up the Prefect API:
  ```
  prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
  ```
- Create a deployment for your workflow:
  ```
  prefect deployment build workflow.py:material_discovery_workflow -n "material-discovery" -q default
  ```
- Apply the deployment:
  ```
  prefect deployment apply material_discovery_workflow-deployment.yaml
  ```
- Start a Prefect agent:
  ```
  prefect agent start -q default
  ```
- Run your deployment:
  ```
  prefect deployment run material_discovery_workflow/material-discovery
  ```

### 6. AWS Lambda Deployment
- Build and push Docker image to AWS ECR.
- Create Lambda function using the Docker image.
- Configure necessary IAM roles and permissions.

### 7. Run and Test Prefect Workflow with AWS Lambda
- Ensure your AWS Lambda function is deployed and accessible.
- Update the `run_simulation` task in `workflow.py` to call your deployed Lambda function.
- Run the Prefect workflow again to verify it correctly interacts with the Lambda function:
  ```
  prefect deployment run material_discovery_workflow/material-discovery
  ```
- Check the Prefect UI (http://127.0.0.1:4200) to monitor the workflow execution and results.

### 8. Update README.md
After successfully implementing and testing all components, update this README.md file with the following information:

- Project Overview: Provide a brief description of your implementation and its purpose.
- AWS Lambda Deployment Process: 
  - Detailed steps you followed to deploy your Lambda function.
  - Any challenges faced and how you resolved them.
- Prefect Workflow Structure:
  - Explain the structure of your workflow.
  - Describe each task and how they interact.
- Performance Analysis:
  - Compare local execution vs. cloud execution.
  - Discuss aspects like speed, scalability, and cost.
- Challenges and Solutions:
  - Describe any significant challenges you encountered during the project.
  - Explain how you overcame these challenges.

### 9. Final Checks and Submission
- Ensure all components are working as expected:
  - Simulator
  - Lambda function
  - Prefect workflow
- Run the check script:
  ```
  python check_submission.py
  ```
- Address any issues highlighted by the check script.
- Commit and push your changes:
  ```
  git add .
  git commit -m "Complete on-demand cloud simulation assignment"
  git push origin main
  ```
- Verify that the GitHub Actions workflow runs successfully:
  - Go to the "Actions" tab in your GitHub repository.
  - Check that all autograding checks have passed.
  - If any checks fail, review the error messages, make necessary corrections, and push again.

## Submission Checklist
Before final submission, ensure you have completed the following:

- [ ] Implemented and tested the material property simulator
- [ ] Created and deployed AWS Lambda function
- [ ] Developed and tested Prefect workflow
- [ ] Successfully integrated Lambda function with Prefect workflow
- [ ] Updated README.md with all required information
- [ ] Passed all checks in check_submission.py
- [ ] Pushed all changes to GitHub
- [ ] GitHub Actions workflow completed successfully

Congratulations on completing the On-Demand Cloud Simulations for Materials Discovery project!
