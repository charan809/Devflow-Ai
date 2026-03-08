🚀 DevFlow: AI-Powered Task Architect
DevFlow is a next-generation project management tool that integrates Generative AI and Machine Learning to automate the software development lifecycle. Built with Django, it doesn't just track tasks—it architects them.

🌟 Key Features
AI Task Breakdown: Uses Google Gemini 2.0 to generate technical sub-tasks for any development goal.

Predictive Analytics: Implements a Scikit-learn Linear Regression model to predict project duration based on complexity.

Role-Based Access (RBAC): Separate interfaces for regular users and administrators.

Automated Workflow: Includes a custom reset_db.py script for rapid environment setup and database recovery.

Modern UI: A clean, responsive dashboard styled with CSS3 variables.

🛠️ Tech Stack
Framework: Django (Python)

AI/ML: Google Gemini API, Scikit-learn, Pandas

Database: SQLite3

Frontend: HTML5, CSS3 (Custom Styles)

⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/yourusername/DevFlow.git
cd DevFlow
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment:
Create a .env file and add your Gemini API Key:


GEMINI_API_KEY=your_api_key_here
Initialize Database:
Run the automated reset script to migrate data and create the default 

admin:
Here are the credentials for your Superuser (Admin) account:

Username: admin
Password: admin123

python reset_db.py
Run Server:
python manage.py runserver
