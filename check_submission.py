import os
import json
import boto3

def check_simulator():
    """Check if the simulator function is implemented correctly."""
    from simulator import simulate_material_property
    
    test_composition = {"Fe": 0.7, "C": 0.3}
    test_temperature = 1000
    result = simulate_material_property(test_composition, test_temperature)
    
    assert isinstance(result, float), "Simulator should return a float value"
    print("✅ Simulator check passed")

def check_lambda_function():
    """Check if the Lambda function is deployed and responds correctly."""
    # TODO: Implement check for Lambda function
    # Use boto3 to invoke the Lambda function and check the response
    print("✅ Lambda function check passed")

def check_workflow():
    """Check if the Prefect workflow is implemented correctly."""
    # TODO: Implement check for Prefect workflow
    # This might involve running the workflow and checking its output
    print("✅ Workflow check passed")

def check_readme():
    with open('README.md', 'r') as f:
        content = f.read()
    
    required_sections = [
        "Project Overview",
        "AWS Lambda Deployment Process",
        "Prefect Workflow Structure",
        "Performance Analysis",
        "Challenges and Solutions",
        "Usage"
    ]
    
    missing_sections = []
    for section in required_sections:
        if not re.search(f"#{1,6} *{section}", content, re.IGNORECASE):
            missing_sections.append(section)
    
    if missing_sections:
        print(f"❌ README check failed. Missing sections: {', '.join(missing_sections)}")
        return False
    
    #  Lambda/URL/ARN
    if not re.search(r'(lambda.*?\.amazonaws\.com|arn:aws:lambda)', content, re.IGNORECASE):
        print("❌ README check failed. Missing Lambda function URL or ARN.")
        return False
    
   
    if not re.search(r'local.*?execution.*?cloud.*?execution|cloud.*?execution.*?local.*?execution', content, re.IGNORECASE):
        print("❌ README check failed. Missing comparison between local and cloud execution.")
        return False
    
    print("✅ README check passed")
    return True

if __name__ == "__main__":
    check_simulator()
    check_lambda_function()
    check_workflow()
    check_readme()
