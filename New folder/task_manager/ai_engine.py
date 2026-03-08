import os
import numpy as np
import google.generativeai as genai
from sklearn.linear_model import LinearRegression
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

def predict_duration(complexity):
    """
    Predicts task duration based on complexity (1-5) using Linear Regression.
    """
    # Training data: [Complexity]
    X = np.array([[1], [2], [3], [4], [5]])
    # Target data: [Hours]
    y = np.array([2, 5, 12, 24, 40]) 
    
    # Train the ML model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict based on the user's input complexity
    prediction = model.predict([[complexity]])
    
    return round(float(prediction[0]), 1)

def get_ai_subtasks(title):
    """
    Uses Gemini Generative AI to break a task title into 3 technical sub-tasks.
    The API Key is pulled securely from the .env file.
    """
    # Securely retrieve the key from environment variables
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "Error: GEMINI_API_KEY not found in .env file."

    # Configure the Google AI library
    genai.configure(api_key=api_key)
    
    # Setup the Generative Model
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Prompt engineering for the LLM
    prompt = (
        f"Act as a Senior Software Engineer. Break down the following task "
        f"into exactly 3 concise, technical bullet points. "
        f"Task: {title}"
    )
    
    try:
        # Generate the response
        response = model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
        # Fallback sub-tasks if the API fails or the key is invalid
        print(f"AI Error: {e}")
        return (
            "1. Define requirements and setup environment\n"
            "2. Implement core functionality and logic\n"
            "3. Run unit tests and perform code cleanup"
        )